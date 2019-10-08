package erratum

// Use uses a resource with an input.
func Use(o ResourceOpener, input string) (err error) {
	var res Resource

	// Try to open.
	for res, err = o(); err != nil; res, err = o() {
		if _, ok := err.(TransientError); ok {
			// Retry on TransientError.
			continue
		}
		return err
	}
	defer res.Close()

	// Recover on a panic.
	defer func() {
		if r := recover(); r != nil {
			if f, ok := r.(FrobError); ok {
				res.Defrob(f.defrobTag)
			}
			err = r.(error)
		}
	}()

	res.Frob(input)
	// A named return must be used to set the
	// return value from inside the defer.
	return err
}
