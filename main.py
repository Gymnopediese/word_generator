from word_gen import *
from saving import *
from inputs.inputs import *
from inputs.ask import *

def main():
    agent = WordGenAgent()
    while 1:
        option = ask_options("menu.txt", 1, 4)
        if option == 1:
            file = ask_folder("txt")
            num = input_int_range("input a number of letter to train on, min 1 and max 5",
                                                "not a valid number try again", 1, 5)
            agent.train(file, num)
        elif option == 2:
            file = ask_folder("snp")
            agent.load(file)
            num = input_int_range("how many word do you want to generate?",
                                  "number too high ot too low", 0, 10000)
            for i in range(num):
                agent.gen_random_word()
        else:
            file = ask_folder("snp")
            agent.load(file)
            agent.save_as_table(file.replace("snp", "xlsx"))


if __name__ == '__main__':
    main()
