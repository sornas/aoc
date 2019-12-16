import math

class Chem(object):
    def __init__(self, name, created):
        self.name = name
        self.created = created

        self.amount = 0
        self.wants = 0
        self.left_over = 0
        self.producers = {}

    def add_producer(self, producer, amount):
        self.producers[producer] = amount

    def queue(self, amount):
        self.wants = amount
        for producer, amount in self.producers.items():
            #TODO
            pass

    def produce(self, amount):
        if self.name == "ORE":
            self.amount += amount
            return

        productions = math.ceil(amount / self.created)
        self.amount += productions * self.created
        for producer, amount in self.producers.items():
            producer.produce(productions * amount)

    def __repr__(self):
        return str((self.name, self.amount))

def pt1(input):
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

    chems["FUEL"].produce(1)
    return chems["ORE"]

def pt2(input):
    return
