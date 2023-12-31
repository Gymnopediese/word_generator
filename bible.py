import random
import progress_bar
from synapse import Synapse

def split_word(word, num = 2):
    a = ""
    l = []
    for i in word:
        a += i
        if (len(a) == num):
            l.append(a.upper())
            a = ""
    if a == "":
        l[-1] += " "
    else:
        while len(a) != num:
            a += " "
            l.append(a.upper())
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
    for i in range(len(syllabs) - 1):
        ind = value_index(synaps, syllabs[i])
        if ind == -1:
            synaps.append(Synapse(syllabs[i], syllabs[i + 1], i + num))
        else:
            synaps[ind].add_synaps(syllabs[i + 1], i + num)


def train_model(num, filename = "dico.txt"):
    with open(filename) as e:
        words = e.read().split("\n")
    synaps = []
    for i in range(len(words)):
        if (words[i] == ""):
            continue
        add_word(split_word(words[i], num), synaps, 0)
        progress_bar.printProgressBar(i, len(words), "the AI is learing")
    return synaps

def gen_random_word(synaps):
    start = get_start(synaps)
    next = start.next_syllab()
    res = start.value
    while " " not in next:
        res += next
        start = synaps[value_index(synaps, next)]
        next = start.next_syllab()
    res += next
    print(res)

def gen_word_from(synaps, start):
    res = start
    start = synaps[value_index(synaps, start[-2:])]
    next = start.next_syllab()
    while " " not in next:
        res += next
        start = synaps[value_index(synaps, next)]
        next = start.next_syllab()
    res += next
    print(res)