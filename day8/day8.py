#!/usr/bin/python
import operator
def get_data():
    with open('input.txt', 'r') as f:
        data = [s.strip().split() for s in f.readlines()]
    return [[str(j) for j in i] for i in data]

def change_num(dict, reg, ins, num):
    if ins == "inc":
        dict[reg] += num
        return
    elif ins == "dec":
        dict[reg] -= num 
        return

def part_one():
    data = get_data()
    dict = {}
    dictMax = {}
    for line in data:
        reg, ins, num, bs, reg2, sign, num2 = line
        num = int(num)
        num2 = int(num2)
        if not dict.has_key(reg):
            dict[reg] = 0
        if not dict.has_key(reg2):
            dict[reg2] = 0
        exp = str(dict[reg2]) + sign + str(num2)

        if eval(exp):
            change_num(dict, reg, ins, num)

    print max(dict.iteritems(), key=operator.itemgetter(1))[1]

def part_two():
    data = get_data()
    dict = {}
    dictMax = {}
    for line in data:
        reg, ins, num, bs, reg2, sign, num2 = line
        num = int(num)
        num2 = int(num2)
        if not dict.has_key(reg):
            dict[reg] = 0
        if not dict.has_key(reg2):
            dict[reg2] = 0
        exp = str(dict[reg2]) + sign + str(num2)

        if eval(exp):
            change_num(dict, reg, ins, num)

        if not dictMax.has_key(reg):
            dictMax[reg] = dict[reg]
        elif dictMax[reg] < dict[reg]:
            dictMax[reg] = dict[reg]

    print max(dictMax.iteritems(), key=operator.itemgetter(1))[1]

if __name__ == "__main__":
    part_one()
    part_two()
