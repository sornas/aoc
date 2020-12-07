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


def graph(bags):
    print("digraph G {")
    print("rankdir=\"LR\";")
    for bag in bags.values():
        for child in bag.children:
            print(f"\"{bag.name}\" -> \"{child[0].name}\" [ label=\"{child[1]}\" ];")
    print("}")


def parse(_in):
    bags = {}  # bag: node
    for bag in _in:
        match = re.match(r"(\w+ \w+) bags contain (no other bags|(((\d+) (\w+ \w+)) bags?(, )?)+)\.",
                         bag)
        children = [(kind, int(count)) for count, kind in zip(match.captures(5),
                                                              match.captures(6))]
        bags[match[1]] = Node(match[1], children)
    for name, bag in bags.items():
        bags[name].children = [(bags[bag], amount) for bag, amount in bags[name].children]
    return bags


def pt1(_in):
    @functools.cache
    def can_contain(bag, target):
        return target in bag or any(can_contain(child, target) for child in bag)

    bags = parse(_in)
    return len([bag for bag in bags.values() if can_contain(bag, bags["shiny gold"])])


def pt2(_in):
    @functools.cache
    def count_children(bag):
        return 1 + sum([child[1] * count_children(child[0]) for child in bag.children])

    bags = parse(_in)
    return count_children(bags["shiny gold"]) - 1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input = open(sys.argv[1], "r").readlines()
    else:
        input = open("../input/07", "r").readlines()
    # graph(parse(input))

    print(pt1(input))
    print(pt2(input))
