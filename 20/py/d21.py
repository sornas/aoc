import aoc20
import sys
import itertools
from collections import defaultdict


def ingredients(line):
    return line[:line.find(" (")].split(" ")


def allergens(line):
    return line[line.find(" (contains ")+len(" (contains "):-2].split(", ")


def pt1(_in):
    all_ingredients = list(itertools.chain.from_iterable(ingredients(line) for line in _in))

    might_be = defaultdict(lambda: set(all_ingredients))
    for line in _in:
        for alg in allergens(line):
            might_be[alg] &= set(ingredients(line))
    return sum(all_ingredients.count(ing)
               for ing in set(all_ingredients) - set.union(*might_be.values()))


def pt2(_in):
    all_ingredients = []
    for line in _in:
        all_ingredients.extend(ingredients(line))

    might_be = defaultdict(lambda: set(all_ingredients))
    for line in _in:
        for alg in allergens(line):
            might_be[alg] &= set(ingredients(line))
    print(might_be)


if __name__ == "__main__":
    _in = aoc20.read_input(sys.argv[1:], 21)
    print(pt1(_in))
    print(pt2(_in))
