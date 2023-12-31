import glob

def ask_folder(path):
    f = glob.glob(f"{path}/*")
    res = ""
    for i in range(len(f)):
        res += f"[{i + 1}] {f[i].split('/')[1]}\n"
    res = res[:-1]
    inp = input_int_range(res, "invalid option", 0, len(f) + 1)
    if inp == 0:
        return None
    return f[inp - 1]

def input_int_range(text1, text2, min, max):
    while True:
        img = input(text1 + "\n>> ")
        try:
            int(img)
            if not (int(img) < min or int(img) >= max):
                return int(img)
            print(text2)
        except:
            print(text2)

def ask_options(path, min, max):
    with open(path) as e:
        return input_int_range(e.read(), "invalid option", min, max)

def ask_y_n_Y_N(message):
    while True:
        print(message)
        inp = input(">>> ")
        if inp == "y" or inp == "yes":
            return 0
        elif inp == "n" or inp == "no":
            return 1
        if inp == "Y" or inp == "YES":
            return 2
        elif inp == "N" or inp == "NO":
            return 3
        else:
            print("please enter a valid answer.")

def ask_y_n(message):
    while True:
        print(message)
        inp = input(">>> ")
        if inp == "y" or inp == "yes":
            return 0
        elif inp == "n" or inp == "no":
            return 1
        else:
            print("please enter a valid answer.")