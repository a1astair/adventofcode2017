#!/usr/bin/python
def get_data():
    with open('captcha.txt', 'r') as f:
        data = [s.strip().split('\t') for s in f.readlines()]
    return [[int(j) for j in i] for i in data]

def part_one():
    total = 0
    data = get_data()
    for row in data:
        total += max(row)-min(row)

    print total

def part_two():
    data = get_data()
    total = 0
    for row in data:
        for i in row:
            for j in row:
                if i % j == 0 and i > j:
                    total += (i/j)
                    break

    print total

if __name__ == "__main__":
    #part_one()
    part_two()
