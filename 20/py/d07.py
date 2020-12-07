#!/usr/bin/env python3
import sys
import re


class Node:
    def __init__(self, name, children=[]):
        self.name = name
        self.parents = []
        self.children = children

    def bag_children(self):
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


mem = dict()
def can_contain(bag, target):
    if bag in mem:
        return mem[bag]
    if target in bag.bag_children():
        mem[bag] = True
        return True
    for child in bag.bag_children():
        if can_contain(child, target):
            mem[bag] = True
            return True
    mem[bag] = False
    return False


def pt1(_in):
    rules = {}  # bag: node
    for rule in _in:
        match = re.match(r"(\w+ \w+) bags contain (no other bags|[^\.]*)\.",
                         rule)
        children = []
        if match[2] != "no other bags":
            child_matches = re.findall(r"(\d+) (\w+ \w+) bags?(, )?", match[2])
            for child_match in child_matches:
                children.append((child_match[1], int(child_match[0])))
        rules[match[1]] = Node(match[1], children)
    for name, bag in rules.items():
        rules[name].children = [(rules[bag], amount) for bag, amount in rules[name].children]
    #graph(rules)

    ans = 0
    for _, bag in rules.items():
        if can_contain(bag, rules["shiny gold"]):
            ans += 1
    return ans


children = dict()
def count_children(bag):
    if bag in children:
        #print("mem", bag)
        return mem[bag]
    amount = 0
    for child in bag.children:
        amount += child[1] * count_children(child[0])
    return 1 + amount


def pt2(_in):
    rules = {}
    for rule in _in:
        match = re.match(r"(\w+ \w+) bags contain (no other bags|[^\.]*)\.",
                         rule)
        children = []
        if match[2] != "no other bags":
            child_matches = re.findall(r"(\d+) (\w+ \w+) bags?(, )?", match[2])
            for child_match in child_matches:
                children.append((child_match[1], int(child_match[0])))
        rules[match[1]] = Node(match[1], children)
    for name, bag in rules.items():
        rules[name].children = [(rules[bag], amount) for bag, amount in rules[name].children]

    return count_children(rules["shiny gold"]) - 1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input = open(sys.argv[1], "r").readlines()
    else:
        input = open("../input/07", "r").readlines()
    #pt1(input)  # for graph

    print(pt1(input))
    print(pt2(input))
