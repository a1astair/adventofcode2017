#!/usr/bin/python
import itertools
def get_data():
    with open('input.txt', 'r') as f:
        data = [s.strip().split() for s in f.readlines()]
    return [[(j).replace(",", "") for j in i] for i in data]
def part_one():
    seen = set()
    data = get_data()
    for alist in data:
        for item in alist:
            if item in seen:
                seen.remove(item)
                continue
            seen.add(item)
    print sorted(seen)

def part_two():
    print "hi"

if __name__ == "__main__":
    part_one()
    # part_two()