#!/usr/bin/env python3
import aoc20
import sys
import functools


class Node:
    def __init__(self, name, children=[]):
        self.name = name
        self.children = children
        self.parents = []

    def __iter__(self):
        yield from (child for child, _ in self.children)


def parse(_in):
    nodes = {}
    for line in _in:
        line = line.split()
        # muted  lime bags contain 1  wavy  lime bag, 1 vibrant green bag, 3 light yellow bags.
        # 0      1    2    3       4  5     6    7    8 9       10    11  12 13    14     15
        # dotted teal bags contain no other bags.
        if line[4] != "no":
            children = [(" ".join(line[i+1:i+3]), int(line[i+0])) for i in range(4, len(line), 4)]
        else:
            children = []
        name = " ".join(line[0:2])
        nodes[name] = Node(name, children)
    for node in nodes.values():
        node.children = [(nodes[node_str], amount) for node_str, amount in node.children]
        for child in node:
            child.parents.append(node)
    return nodes


def pt1(_in):
    @functools.cache
    def types_above(node):
        return node.parents + list(functools.reduce(lambda a, b: a + b, (types_above(parent) for parent in node.parents), []))

    nodes = parse(_in)
    return len(set(types_above(nodes["shiny gold"])))


def pt2(_in):
    @functools.cache
    def count_children(node):
        return 1 + sum(child[1] * count_children(child[0]) for child in node.children)

    nodes = parse(_in)
    return count_children(nodes["shiny gold"]) - 1


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 7)
    # graph(parse(input))
    print(pt1(input))
    print(pt2(input))
