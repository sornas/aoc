import re
import sys

def new_level(old, op):
    return eval(op.split(" = ")[1])

def main():
    monkeys = sys.stdin.read().split("\n\n")
    parsed = []
    for monkey in monkeys:
        if not monkey.strip():
            continue
        match = re.search(r"Monkey (\d):\s*Starting items: ((\d*(, )?)+)\s*Operation: (([^\n])+)\s*Test: divisible by (\d+)\s*If true: throw to monkey (\d+)\s*If false: throw to monkey (\d+)", monkey, re.MULTILINE)
        monkey, items, _, _, operation, _, test, if_true, if_false = list(match.groups())
        items = list(map(int, items.split(", ")))
        parsed.append((int(monkey), items, operation, int(test), int(if_true), int(if_false)))
    inspected = [0 for _ in range(len(parsed))]
    all_divs = 1
    for monkey in parsed:
        all_divs *= monkey[3]
    # for _ in range(20):
    for r in range(10000):
        print(r)
        for monkey in parsed:
            for _ in range(len(monkey[1])):
                inspected[monkey[0]] += 1
                item = monkey[1].pop(0)
                item = new_level(item, monkey[2])
                item %= all_divs
                # item //= 3
                if item % monkey[3] == 0:
                    parsed[monkey[4]][1].append(item)
                else:
                    parsed[monkey[5]][1].append(item)

    inspected.sort()
    print(inspected[-1]*inspected[-2])

main()
