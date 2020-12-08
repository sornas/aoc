#!/usr/bin/env python3
import sys
import regex as re
import functools


class Node:
    def __init__(self, name, children=[]):
        self.name = name
        self.children = children

    def __iter__(self):
        for child in self.children:
            yield child[0]

    def __repr__(self):
        return self.name


def graph(nodes):
    print("digraph G {")
    print("rankdir=\"LR\";")
    for node in nodes.values():
        for child in node.children:
            print(f"\"{node.name}\" -> \"{child[0].name}\" [ label=\"{child[1]}\" ];")
    print("}")


def parse(_in):
    nodes = {}
    for line in _in:
        match = re.match(r"(\w+ \w+) bags contain (no other bags|(((\d+) (\w+ \w+)) bags?(, )?)+)\.", line)
        children = [(node_str, int(amount)) for amount, node_str in zip(match.captures(5), match.captures(6))]
        nodes[match[1]] = Node(match[1], children)
    for node in nodes.values():
        node.children = [(nodes[node_str], amount) for node_str, amount in node.children]
    return nodes


def pt1(_in):
    @functools.cache
    def can_contain(node, target):
        return target in node or any(can_contain(child, target) for child in node)

    nodes = parse(_in)
    return len([node for node in nodes.values() if can_contain(node, nodes["shiny gold"])])


def pt2(_in):
    @functools.cache
    def count_children(node):
        return 1 + sum([child[1] * count_children(child[0]) for child in node.children])

    nodes = parse(_in)
    return count_children(nodes["shiny gold"]) - 1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input = open(sys.argv[1], "r").readlines()
    else:
        input = open("../input/07", "r").readlines()
    # graph(parse(input))

    print(pt1(input))
    print(pt2(input))
