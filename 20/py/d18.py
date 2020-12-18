#!/usr/bin/env python3
import aoc20
import sys
from collections import deque
from itertools import islice


def find_closing_paren(expr):
    parens = 0
    for i, token in enumerate(expr):
        if token == "(":
            parens += 1
        elif token == ")":
            if parens == 0:
                return i
            parens -= 1
    print("can't find closing parenthesis")
    return None


def eval_expr1(expr):
    if not expr:
        print("empty expression")
        return None
    cur = expr.popleft()
    if cur == "(":
        closing = find_closing_paren(expr)
        left = eval_expr1(deque(islice(expr, closing)))
        expr = deque(islice(expr, closing+1, None))
    else:
        while cur == ")":
            cur = expr.popleft()
        left = int(cur)
    if not expr:
        return left
    oper = expr.popleft()
    right = eval_expr1(expr)
    if oper == "+":
        return left + right
    elif oper == "*":
        return left * right
    else:
        print("unkown oper", oper)
        return None


def pt1(_in):
    res = 0
    for line in _in:
        line = deque(line.replace(")", "a")    # yikes
                         .replace("(", "b")    # yikes
                         .replace("a", " ( ")  # yikes
                         .replace("b", " ) ")  # yikes
                         .split()[::-1])       # YIKES
        res += eval_expr1(line)
    return res


def pt2(_in):
    pass


if __name__ == "__main__":
    input = aoc20.read_input(sys.argv[1:], 18)
    print(pt1(input))
    print(pt2(input))
