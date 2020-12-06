class Cell(object):

  def __init__(self):
    self.watchers = set()

  def add_watcher(self, o):
    # Add a watcher cell that needs updating when this cell updates.
    self.watchers.add(o)


class InputCell(Cell):

  def __init__(self, initial_value):
    self._value = initial_value
    super(InputCell, self).__init__()

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, v):
    if self._value == v:
      return
    self._value = v
    self.notify()

  def notify(self):
    # Build breadth-first unique recursive set of watchers.
    notify_list = []
    check = list(self.watchers)
    while check:
      n = check.pop(0)
      if n in notify_list:
        continue
      notify_list.append(n)
      check.extend(n.watchers)

    for n in notify_list:
      n.updated()


class ComputeCell(Cell):
  def __init__(self, inputs, compute_function):
    self.inputs = inputs
    self.compute_function = compute_function

    self.callbacks = set()
    self.value = None
    self.compute_value()

    for i in self.inputs:
      if isinstance(i, Cell):
        i.add_watcher(self)
    super(ComputeCell, self).__init__()

  def compute_value(self):
    v = self.compute_function([v.value for v in self.inputs])
    self.changed = v != self.value
    self.value = v

  def add_callback(self, callback):
    self.callbacks.add(callback)

  def remove_callback(self, callback):
    if callback in self.callbacks:
      self.callbacks.remove(callback)

  def updated(self):
    self.compute_value()
    if self.changed:
      for c in self.callbacks:
        c(self.value)

# vim:ts=2:sw=2:expandtab
