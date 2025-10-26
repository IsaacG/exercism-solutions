package react

import "slices"

// MyCell is a Cell which supports both callbacks and dependent compute cells.
type MyCell interface {
	Cell

	addDep(*computeCell)
	dependents() []*computeCell
	runCallbacks()
}

// ======== myCell ========

// myCell implements MyCell.
type myCell struct {
	// value is the cell's value.
	value int
	// callbacks are called when the value changes.
	callbacks []func(int)
	// deps are updated when the value changes.
	deps []*computeCell
}

// runCallbacks runs all the cell's callbacks, skipping nil functions.
func (c *myCell) runCallbacks() {
	for _, callback := range c.callbacks {
		if callback != nil {
			callback(c.Value())
		}
	}
}

func (c *myCell) dependents() []*computeCell {
	return c.deps
}
func (c *myCell) addDep(dep *computeCell) {
	c.deps = append(c.deps, dep)
}

func (c *myCell) AddCallback(callback func(int)) Canceler {
	c.callbacks = append(c.callbacks, callback)
	// Reference the callback by index.
	return &canceler{len(c.callbacks) - 1, c}
}

func (c *myCell) Value() int {
	return c.value
}

// ======== computeCell ========

// computeCell implements ComputeCell, using a compute function and inputs to update the value.
type computeCell struct {
	myCell
	compute func() int
}

// maybeUpdate recomputes the cell's value and returns if the value changed.
func (c *computeCell) maybeUpdate() bool {
	computed := c.compute()
	if computed == c.value {
		return false
	}
	c.value = computed
	return true
}

// ======== inputCell ========

// inputCell implements InputCell.
type inputCell struct {
	myCell
}

// recursiveDependents recursively collects all dependent computeCells.
func (c *inputCell) recursiveDependents() []*computeCell {
	var impacted, new []*computeCell
	new = c.deps
	for new != nil {
		impacted = append(impacted, new...)
		var discovered []*computeCell
		for _, cell := range new {
			for _, dep := range cell.dependents() {
				if !slices.Contains(impacted, dep) {
					discovered = append(discovered, dep)
				}
			}
		}
		new = discovered
	}
	return impacted
}

// Update the cell's value and trigger recursive callbacks.
func (c *inputCell) SetValue(value int) {
	if c.value == value {
		return
	}
	c.value = value
	c.runCallbacks()

	for _, cell := range c.recursiveDependents() {
		if cell.maybeUpdate() {
			cell.runCallbacks()
		}
	}

}

// ======== canceler ========

// canceler implements Canceler.
type canceler struct {
	// idx is the index of the callback function in the cell.
	idx  int
	cell *myCell
}

// Cancel replaces a specific callback function with nil, canceling it.
func (c *canceler) Cancel() {
	c.cell.callbacks[c.idx] = nil
}

// ======== reactor ========

type reactor struct{}

// New returns a new Reactor.
func New() Reactor {
	return &reactor{}
}

func (r *reactor) CreateInput(initial int) InputCell {
	c := &inputCell{
		myCell{value: initial},
	}
	return c
}

func (r *reactor) CreateCompute1(dep Cell, compute func(int) int) ComputeCell {
	c := &computeCell{
		compute: func() int { return compute(dep.Value()) },
	}
	c.value = c.compute()
	dep.(MyCell).addDep(c)
	return c
}

func (r *reactor) CreateCompute2(dep1, dep2 Cell, compute func(int, int) int) ComputeCell {
	c := &computeCell{
		compute: func() int { return compute(dep1.Value(), dep2.Value()) },
	}
	c.value = c.compute()
	dep1.(MyCell).addDep(c)
	dep2.(MyCell).addDep(c)
	return c
}
