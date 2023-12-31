import random
import progress_bar
from synapse import Synapse

def split_word(word, num = 2):
    a = ""
    l = []
    i = 0
    j = 0
    while i < len(word):
        if len(a) == num or i + j >= len(word):
            while len(a) != num:
                a += " "
            l.append(a.upper())
            a = ""
            i += 1
            j = 0
        if i + j >= len(word):
            break
        a += word[i + j]
        j += 1
    l.append(" " * num)
    return l

def value_index(synaps, syllab):
    for k in range(len(synaps)):
        if synaps[k].value == syllab:
            return k
    return -1


def get_start(synaps):
    ind = []
    for i in range(len(synaps)):
        if synaps[i].start:
            ind.append(i)
    return synaps[ind[random.randint(0, len(ind) - 1)]]

def add_word(syllabs, synaps, num=0):
    for i in range(len(syllabs) - num):
        ind = value_index(synaps, syllabs[i])
        if ind == -1:
            synaps.append(Synapse(syllabs[i], syllabs[i + num], i))
        else:
            synaps[ind].add_synaps(syllabs[i + num], i)

def train_model(num, filename = "dico.txt"):
    with open(filename) as e:
        words = e.read().split("\n")
    synaps = []
    for i in range(len(words)):
        if (words[i] == ""):
            continue
        add_word(split_word(words[i], num), synaps, num)
        progress_bar.printProgressBar(i, len(words), "the AI is learing")
    return synaps
