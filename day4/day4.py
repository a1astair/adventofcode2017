#!/usr/bin/python
def get_data():
    with open('input.txt', 'r') as f:
        data = [s.strip().split('\t') for s in f.readlines()]
    return [[int(j) for j in i] for i in data]

def part_one():
    count = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            lineset = set()
            for word in line.split():
                if word not in lineset:
                    # Doesn't exist in list so add it on
                    lineset.add(word)
                else:
                    count -= 1
                    break
            count += 1
    print count

def part_two():
    count = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            linelist = []
            for word in line.split():
                linelist.append(''.join(sorted(word)))
            linelist.sort()
            if len(linelist) == len(set(linelist)):
                count += 1
    print count

if __name__ == "__main__":
    # part_one()
    part_two()
