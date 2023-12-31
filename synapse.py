import random

class Synapse:
    value = ""
    start = False
    synaps = []
    weight = []
    def __init__(self, value, new, start):
        self.start = False
        if start == 0:
            self.start = True
        self.value = value
        self.synaps = []
        self.weight = []
        if None != new:
            self.synaps.append(new)
            self.weight.append(1)
    def add_synaps(self, new, start):
        if (start) == 0:
            self.start = True
        try:
            ind = self.synaps.index(new)
            self.weight[ind] += 1
        except:
            self.synaps.append(new)
            self.weight.append(1)
    def next_syllab(self):
        weight = []
        for i in range(len(self.weight)):
            for k in range(self.weight[i]):
                weight.append(i)
        res = self.synaps[weight[random.randint(0, len(weight) - 1)]]
        #if " " in res and random.randint(0,1) == 0:
        #    return self.next_syllab()
        return res

    def __contains__(self, key):
        pass

    def __str__(self):
        return self.value + "\n" + str(self.synaps) + "\n" + str(self.weight)
