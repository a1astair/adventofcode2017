#!/usr/bin/python
import operator

input = 329

def part_one():
    spinlock = [0]
    i, position = 1, 0
    for i in range(1, 2017):
        spinlen = len(spinlock)
        position = (position + input) % spinlen + 1
        spinlock.insert(position, i)
    print spinlock[spinlock.index(2017)+1]

def part_two():
    i, position, spinlen, answer = 1, 0, 1, 0
    for i in range(1, 50000001):
        # Not using a list anymore but still need to increment length
        position = (position + input) % spinlen + 1
        if position == 1:
            answer = i
        spinlen += 1
    print answer

if __name__ == "__main__":
    part_one()
    # part_two()
