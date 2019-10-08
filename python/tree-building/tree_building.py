class Record():
  def __init__(self, record_id, parent_id):
    self.record_id = record_id
    self.parent_id = parent_id


class Node():
  def __init__(self, node_id):
    self.node_id = node_id
    self.children = []


def BuildTree(records):
  if not records:
    return None

  nodes = {}
  records.sort(key=lambda x: x.record_id)

  for record in records:
    if record.record_id == 0:
      if record.parent_id != 0:
        raise ValueError('Root node cannot have a parent')
    elif record.record_id == record.parent_id:
      raise ValueError('Tree is a cycle')
    if record.record_id < record.parent_id:
      raise ValueError('Parent id must be lower than child id')

    nodes[record.record_id] = Node(record.record_id)

  if 0 not in nodes:
    raise ValueError('Tree must start with id 0')
  if sorted(nodes.keys()) != list(range(len(nodes))):
    raise ValueError('Tree must be continuous')

  for record in records:
    if record.record_id == 0:
      continue
    nodes[record.parent_id].children.append(nodes[record.record_id])
  
  return nodes[0]


# vim:ts=2:sw=2:expandtab
