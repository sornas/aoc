from typing import Iterable
import sys

class Tree(object):
    # https://stackoverflow.com/a/28015122
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        self.parent = None
        if children is not None:
            for child in children:
                self.add_child(child)
    def add_child(self, node):
        self.children.append(node)
        node.parent = self

    def __eq__(self, other):
        if isinstance(other, Tree):
            return self.name == other.name
        return False
    def parents(self):
        return [self.parent] + self.parent.parents() if self.parent != None\
                else []

def gen_tree(input):
    trees = {}
    seen = set()  # seen trees. contains only IDs
    leafs = {}

    for orbit in input:
        orbit = orbit.split(")")
        #print(orbit)
        if not orbit[0] in seen:
            trees[orbit[0]] = Tree(orbit[0])
            seen.add(orbit[0])

    # hook up each child to its parent (since every parent now exists)
    for orbit in input:
        orbit = orbit.rstrip().split(")")
        if orbit[1] in seen:
            trees[orbit[0]].add_child(trees[orbit[1]])
        else:
            leafs[orbit[1]] = Tree(orbit[1])
            trees[orbit[0]].add_child(leafs[orbit[1]])
    for k in trees:
        pass
        #print(trees[k], trees[k].children)

    trees.update(leafs)
    return trees

sum_depths = 0
def pt1(input):
    tree = gen_tree(input)
    depth = 0
    depths = {}
    def count_children(tree, depth):
        global sum_depths  # fusk-rekursion? ville bara att det skulle fungera
        sum_depths += depth
        depths[tree.name] = depth
        for child in tree.children:
            count_children(child, depth+1)
    count_children(tree["COM"], 0) 
    return sum_depths

def pt2(input):
    # find common parent and distance to it
    tree = gen_tree(input)
    src_parents = tree["YOU"].parent.parents()
    tar_parents = tree["SAN"].parent.parents()
    src_dist = 0
    for src_parent in src_parents:
        src_dist += 1
        tar_dist = 0
        for tar_parent in tar_parents:
            tar_dist += 1
            if src_parent == tar_parent:
                return (src_parent.name, src_dist, tar_dist, src_dist + tar_dist)

if __name__ == "__main__":
    import cProfile

    input = open("../input/06", "r").readlines()
    cProfile.run("pt1(input)")
    cProfile.run("pt2(input)")
    print(pt1(input))
    print(pt2(input))
