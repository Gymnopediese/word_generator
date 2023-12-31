from word_gen import *

class WordGenAgent:

    def __init__(self, file = ""):
        self.synapses = []
        if file != "":
            self.load(file)
        self.num = 0

    def save(self, filename, num):
        self.synapses.sort(key=lambda x: x.value)
        self.num = num
        res = str(num) + "\n"
        for i in self.synapses:
            num = []
            for k in i.weight:
                num.append(str(k))
            res += i.value + "$" + ":".join(i.synaps) + "$" + ":".join(num) + "$" + str(i.start) + "\n"
        with open(filename, 'w') as e:
            e.write(res)

    def save_as_table(self, filename):
        import xlsxwriter
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()
        self.synapses.sort(key=lambda x: x.value)
        for i in range(len(self.synapses)):
            worksheet.write(0, i + 1, self.synapses[i].value)
            worksheet.write(i + 1, 0, self.synapses[i].value)
        worksheet.write(len(self.synapses) + 1, 0, "Total")
        for i in range(len(self.synapses)):
            worksheet.write(len(self.synapses) + 1, i + 1, sum(self.synapses[i].weight))
        for i in range(len(self.synapses)):
            for k in range(len(self.synapses)):

                try:
                    index = self.synapses[i].synaps.index(self.synapses[k].value)
                    worksheet.write(i + 1, k + 1, self.synapses[i].weight[index])
                except ValueError as e:
                    worksheet.write(i + 1, k + 1, "X")
        workbook.close()

    def load(self, filename):
        self.synapses = []
        with open(filename) as e:
            lines = e.read().split("\n")
        self.num = int(lines[0])
        lines.remove(lines[0])
        for i in lines:
            if i == "":
                continue
            sp = i.split("$")
            start = 0
            if (sp[-1] == "False"):
                start = 10
            synap = Synapse(sp[0], None, start)
            synaps = sp[1].split(":")
            weight = sp[2].split(":")
            for k in weight:
                synap.weight.append(int(k))
            synap.synaps = synaps
            self.synapses.append(synap)


    def train(self, filename: str, num):
        self.synapses = train_model(num, filename)
        self.save(filename.replace(".txt", str(num) + ".snp").replace("txt", "snp"), num)

    def gen_random_word(self):
        start = get_start(self.synapses)
        next = start.next_syllab()
        res = start.value
        m = 0
        while " " not in res and m < 10:
            res += next[0]
            i = value_index(self.synapses, res[-self.num:])
            if i == -1:
                break
            start = self.synapses[i]
            next = start.next_syllab()
            m += 1
        print(res)

    def gen_word_from(self, start):
        res = start
        start = self.synapses[value_index(self.synapses, start[-2:])]
        next = start.next_syllab()
        while " " not in next:
            res += next
            start = self.synapses[value_index(self.synapses, next)]
            next = start.next_syllab()
        res += next
        print(res)