#!/usr/bin/python
def get_data():
    with open('input.txt', 'r') as f:
        for s in f.readlines():
            data = s.strip().split(",")
    return data

def part_one():
    data = get_data()
    ns, ew = 0,0
    steps = 0
    for direction in data:
        if direction == 's':
            ns -=1
        elif direction == 'se':
            ns -= 0.5
            ew += 0.5
        elif direction == 'sw':
            ns -= 0.5
            ew -= 0.5
        elif direction == 'n':
            ns += 1
        elif direction == 'ne':
            ns += 0.5
            ew += 0.5
        elif direction == 'nw':
            ns += 0.5
            ew -= 0.5
    return abs(ew)+abs(ns)

def part_two():
    data = get_data()
    ns, ew = 0,0
    my_max = 0
    for direction in data:
        if direction == 's':
            ns -=1
        elif direction == 'se':
            ns -= 0.5
            ew += 0.5
        elif direction == 'sw':
            ns -= 0.5
            ew -= 0.5
        elif direction == 'n':
            ns += 1
        elif direction == 'ne':
            ns += 0.5
            ew += 0.5
        elif direction == 'nw':
            ns += 0.5
            ew -= 0.5
        my_max = max(my_max, abs(ew) + abs(ns))
    return abs(ew)+abs(ns), my_max

if __name__ == "__main__":
    print(part_one())
    print(part_two())
