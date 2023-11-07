import dataclasses


@dataclasses.dataclass
class Record:
    record_id: int
    parent_id: int


@dataclasses.dataclass
class Node:
    node_id: int
    def __post_init__(self) -> None:
        self.children: list[Node] = []


def BuildTree(records: list[Record]) -> Node | None:
    if not records:
        return None

    nodes = {}
    records.sort(key=lambda x: x.record_id)

    for record in records:
        if record.record_id != 0 and record.record_id == record.parent_id:
            raise ValueError('Only root should have equal record and parent id.')
        if record.record_id < record.parent_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")

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
