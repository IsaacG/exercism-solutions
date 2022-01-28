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
        raise ValueError("Node record_id should be smaller than it's parent_id.")
    elif record.record_id == record.parent_id:
      raise ValueError('Only root should have equal record and parent id.')
    if record.record_id < record.parent_id:
      raise ValueError("Node record_id should be smaller than it's parent_id.")

    nodes[record.record_id] = Node(record.record_id)

  if 0 not in nodes:
    raise ValueError('Record id is invalid or out of order.')
  if sorted(nodes.keys()) != list(range(len(nodes))):
    raise ValueError('Record id is invalid or out of order.')

  for record in records:
    if record.record_id == 0:
      continue
    nodes[record.parent_id].children.append(nodes[record.record_id])
  
  return nodes[0]


# vim:ts=2:sw=2:expandtab
