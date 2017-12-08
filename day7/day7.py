#!/usr/bin/python
from anytree import Node, RenderTree
def get_data():
    with open('input.txt', 'r') as f:
        data = [s.strip().split() for s in f.readlines()]
    return [[(j).replace(",", "") for j in i] for i in data]

def part_one():
    seen = set()
    data = get_data()
    for alist in data:
        for item in alist:
            if item in seen:
                seen.remove(item)
                continue
            seen.add(item)
    print sorted(seen)

def pop_list(nodes=None, parent=None, node_list=None):
    if parent is None:
        return node_list
    node_list.append([])
    for node in nodes:
        if node['parent'] == parent:
            node_list[-1].append(node)
        if node['id'] == parent:
            next_parent = node['parent']

    pop_list(nodes, next_parent, node_list)
    return node_list

class Node:
    def __init__(self, id, weight, parent):
        self.id = id
        self.weight = weight
        self.parent = parent

    def __repr__(self):
        return("ID: {} weight: {} parent: {}").format(self.id, self.weight, self.parent)


def part_two():
    data = get_data()
    newNodes = []
    for alist in data:
        if len(alist) == 2:
            newNode = Node(alist[0], alist[1], None)
            newNodes.append(newNodes)
        else:
            for i in range(3, len(alist)):
                newNode = Node(alist[0], alist[1], alist[i])
                newNodes.append(newNode)
    root = Node("mwzaxaj")
    while True:
        # TODO: Do some logic here to make a dope tree

if __name__ == "__main__":
    # part_one()
    part_two()