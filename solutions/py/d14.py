import math

class Chem(object):
    def __init__(self, name, created):
        self.name = name
        self.created = created

        self.amount = 0
        self.left_over = 0
        self.producers = {}

    def add_producer(self, producer, amount):
        self.producers[producer] = amount

    def produce(self, to_create):
        if self.name == "ORE":
            self.amount += to_create
            return
        if self.left_over > 0:
            if self.left_over < to_create:
                to_create -= self.left_over
                self.left_over = 0
            else:
                self.left_over -= to_create
                to_create = 0
        productions = math.ceil(to_create / self.created)
        self.amount += productions * self.created
        self.left_over += productions * self.created - to_create
        for producer, amount in self.producers.items():
            producer.produce(productions * amount)

    def __repr__(self):
        return str((self.name, self.amount))

def read_chems(input):
    chems = {"ORE": Chem("ORE", 1)}
    for line in input:
        output = line.strip().split(" => ")[1]
        chems[output.split(" ")[1]] = Chem(output.split(" ")[1], int(output.split(" ")[0]))

    for line in input:
        inputs = line.strip().split(" => ")[0]
        output = line.strip().split(" => ")[1]
        for i in inputs.split(", "):
            chems[output.split(" ")[1]] \
                    .add_producer(chems[i.split(" ")[1]], int(i.split(" ")[0]))
    return chems

def pt1(input, amount=1):
    chems = read_chems(input)
    chems["FUEL"].produce(amount)
    return chems["ORE"].amount

def pt2(input):
    low, high = 0, int(1e9)
    target = 1000000000000
    prev_guess = 0
    while low != high:
        guess = (low+high) // 2
        if guess == prev_guess:
            break
        prev_guess = guess
        chems = read_chems(input)
        chems["FUEL"].produce(guess)
        if chems["ORE"].amount == target:
            break
        elif chems["ORE"].amount > target:
            high = guess
        else:
            low = guess
    #print(low, guess, high)
    return guess

if __name__ == "__main__":
    input = open("../input/14", "r").readlines()
    print(pt1(input))
    print(pt2(input))
