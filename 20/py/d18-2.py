import sys

binding = {
    "+": (5, 6),
    "*": (3, 4),
}

class Parser:
    def __init__(self, tokens):
        self.pos = 0
        self.tokens = tokens

    def eof(self):
        return self.pos == len(self.tokens)

    def peek(self):
        return self.tokens[self.pos]

    def eof_next(self):
        return self.pos + 1 == len(self.tokens)

    def peek_next(self):
        return self.tokens[self.pos + 1]

    def eat(self):
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def expr(self, min_bp):
        # left hand side
        match self.eat():
            case "(":
                lhs = self.expr(0)
                assert self.eat() == ")"
            case "+":
                assert False
            case "-":
                assert False
            case lit:
                lhs = int(lit)
        while True:
            if self.eof():
                break
            op = self.peek()
            if op in binding:
                if binding[op][0] < min_bp:
                    break
                self.eat()
                rhs = self.expr(binding[op][1])
                if op == "+":
                    lhs = lhs + rhs
                elif op == "*":
                    lhs = lhs * rhs
                else:
                    assert False
                continue
            break
        return lhs


    # a + b * c
    # -> (a + b) * c
    #
    # a + (b * c) + d
    # -> (a + (b * c)) + d


def main():
    tot = 0
    for line in sys.stdin.read().split("\n"):
        if not line: continue
        parts = [part for part in line if part and part != " "]
        parser = Parser(parts)
        tot += parser.expr(0)
    print(tot)

main()
