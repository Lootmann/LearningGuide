from typing import Optional


class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records: list) -> Optional[Node]:
    if len(records) == 0:
        return None

    root = None
    records.sort(key=lambda x: x.record_id)
    ordered_id = [i.record_id for i in records]

    if records:
        if ordered_id[-1] != len(ordered_id) - 1:
            raise ValueError("Record id is invalid or out of order.")
        if ordered_id[0] != 0:
            raise ValueError("Only root should have equal record and parent id.")

    for record in records:
        if record.parent_id > record.record_id:
            raise ValueError("Node record_id should be smaller than it's parent_id.")

    trees = []

    for i, order_id in enumerate(ordered_id):
        for record in records:
            if order_id == record.record_id:
                if record.record_id == 0 and record.parent_id != 0:
                    raise ValueError("error!")

                if record.record_id < record.parent_id:
                    raise ValueError("something went wrong!")

                if record.record_id == record.parent_id:
                    if record.record_id != 0:
                        raise ValueError(
                            "Only root should have equal record and parent id."
                        )

                trees.append(Node(ordered_id[i]))

    parent = {}

    for _, order_id in enumerate(ordered_id):
        for tree in trees:
            if order_id == tree.node_id:
                parent = tree

        for record in records:
            if record.parent_id == order_id:
                for k in trees:
                    if k.node_id == 0:
                        continue
                    if record.record_id == k.node_id:
                        child = k
                        parent.children.append(child)

    if len(trees) > 0:
        root = trees[0]

    return root
