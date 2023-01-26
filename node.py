import numpy as nb
class Node:
    def __init__(self, value, father=None, depth=0 , cost = 0):
        self.father = father
        self.value = nb.array(value)
        self.depth =  depth
        self.cost = cost
        self.h = cost + depth

    def __lt__(self, other):
        if(self.h == other.h):
            return self.cost < other.cost
        return self.h < other.h
        

    def __hash__(self) -> str:
        hash = ''
        for i in range(len(self.value)):
            for j in range(len(self.value[i])):
                if (self.value[i][j] == ' '):
                    hash += '0'

                elif (self.value[i][j] == '#'):
                    hash += '00'
                else:
                    hash += self.value[i][j]

        return int(hash)
