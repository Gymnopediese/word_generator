
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
voyels = ['a','e','i','o','u','y']
consonnes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']

def voyels_inseparable(a, b, c = 'nn'):
    res = a + b
    if c != 'nn':
        res += c
    return res == 'ou' or res == 'eau' or res == 'ai' or res == 'au'

def word_to_syllabs(word):
    list = []
    current = ""
    i = 0
    imuable = ["br", "gn"]
    while i < len(word):
        current += word[i]
        if i < len(word) - 1 and voyels_inseparable(word[i], word[i + 1]):
            pass
        elif i < len(word) - 2 and voyels_inseparable(word[i], word[i + 1], word[i + 2]):
            pass
        elif i < len(word) - 3 and word[i] in voyels and word[i + 1] in consonnes and word[i + 2] in consonnes and word[i + 3] in consonnes:
            current += word[i + 1]
            current += word[i + 2]
            if i + 4 == len(word):
                current += word[i + 3]
                i += 1
            i += 2
            list.append(current)
            current = ""
        elif i < len(word) - 2 and word[i] in voyels and word[i + 1] in consonnes and word[i + 2] in consonnes:
            current += word[i + 1]
            i += 1
            list.append(current)
            current = ""
        elif word[i] in voyels:
            if i + 2 == len(word):
                current += word[i + 1]
                i += 1
            list.append(current)
            current = ""
        i += 1
    if current != "":
        list.append(current)
    return list

if __name__ == '__main__':
    print(word_to_syllabs("manger"))
    print(word_to_syllabs("printemps"))
    print(word_to_syllabs("elle"))
    print(word_to_syllabs("arreter"))
    print(word_to_syllabs("trousse"))
    print(word_to_syllabs("separer"))
    print(word_to_syllabs("bureau"))
    print(word_to_syllabs("compter"))
    print(word_to_syllabs("montagne"))
    print(word_to_syllabs("marcher"))
    print(word_to_syllabs("telephone"))
    print(word_to_syllabs("thermometre"))

