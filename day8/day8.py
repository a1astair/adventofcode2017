#!/usr/bin/python
import operator, json
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
        reg = line[0]
        ins = line[1]
        num = int(line[2])
        reg2 = line[4]
        sign = line[5]
        num2 = int(line[6])
        if not dict.has_key(reg):
            dict[reg] = 0
        if not dict.has_key(reg2):
            dict[reg2] = 0
        if sign == "<" and dict[reg2] < num2:
            change_num(dict, reg, ins, num)

        elif sign == ">" and dict[reg2] > num2:
            change_num(dict, reg, ins, num)

        elif sign == ">=" and dict[reg2] >= num2:
            change_num(dict, reg, ins, num)
            
        elif sign == "==" and dict[reg2] == num2:
            change_num(dict, reg, ins, num)
                
        elif sign == "!=" and dict[reg2] != num2:
            change_num(dict, reg, ins, num)

        elif sign == "<=" and dict[reg2] <= num2:
            change_num(dict, reg, ins, num)

    print max(dict.iteritems(), key=operator.itemgetter(1))[1]

def part_two():
    data = get_data()
    dict = {}
    dictMax = {}
    for line in data:
        reg = line[0]
        ins = line[1]
        num = int(line[2])
        reg2 = line[4]
        sign = line[5]
        num2 = int(line[6])
        if not dict.has_key(reg):
            dict[reg] = 0
        if not dict.has_key(reg2):
            dict[reg2] = 0
        if sign == "<" and dict[reg2] < num2:
            change_num(dict, reg, ins, num)

        elif sign == ">" and dict[reg2] > num2:
            change_num(dict, reg, ins, num)

        elif sign == ">=" and dict[reg2] >= num2:
            change_num(dict, reg, ins, num)
            
        elif sign == "==" and dict[reg2] == num2:
            change_num(dict, reg, ins, num)
                
        elif sign == "!=" and dict[reg2] != num2:
            change_num(dict, reg, ins, num)

        elif sign == "<=" and dict[reg2] <= num2:
            change_num(dict, reg, ins, num)
        if not dictMax.has_key(reg):
            dictMax[reg] = dict[reg]
        elif dictMax[reg] < dict[reg]:
            dictMax[reg] = dict[reg]

    print max(dictMax.iteritems(), key=operator.itemgetter(1))[1]

if __name__ == "__main__":
    part_one()
    part_two()
