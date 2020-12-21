import aoc20
import sys
from collections import defaultdict
import functools
import re


def pt1(_in):
    rules = dict()
    for rule in "".join(_in).split("\n\n")[0].split("\n"):
        rule = rule.replace("\"", "").split(": ")
        rules[rule[0]] = rule[1] if rule[1] in "ab" else "( {} )".format(rule[1])

    @functools.cache
    def format_rule(rule):
        if rule not in rules:
            return rule
        return " ".join(format_rule(token) for token in rules[rule].split())

    regex = re.compile(format_rule("0").replace(" ", ""))
    return sum(1 for line in "".join(_in).split("\n\n")[1][:-1].split("\n") if regex.fullmatch(line))


def pt2(_in):
    pass


if __name__ == "__main__":
    _in = aoc20.read_input(sys.argv[1:], 19)
    print(pt1(_in))
    print(pt2(_in))
