#!/usr/bin/python
import operator
input = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]

def part_one():
    length = len(input)
    inputs =[]
    inputs.append(input[:])
    count = 0
    while True:
        index, value = max(enumerate(input), key=operator.itemgetter(1))
        # Set index to zero and add one to every following number
        input[index] = 0
        for i in range(index+1, value+index+1):
            input[i%length] += 1
        count +=1
        if input in inputs:
            print count
            return
        inputs.append(input[:])  

def part_two():
    length = len(input)
    inputs =[]
    inputs.append(input[:])
    count = 0
    while True:
        index, value = max(enumerate(input), key=operator.itemgetter(1))
        # Set index to zero and add one to every following number
        input[index] = 0
        for i in range(index+1, value+index+1):
            input[i%length] += 1
        count += 1
        if input in inputs:
            index = inputs.index(input)
            print count-index
            return
        inputs.append(input[:])  


if __name__ == "__main__":
    # part_one()
    part_two()