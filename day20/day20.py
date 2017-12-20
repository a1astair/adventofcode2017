#!/usr/bin/python
import re, operator
from itertools import chain
def get_data():
    with open('input.txt', 'r') as f:
        data = [s.strip().split() for s in f.readlines()]
    return [[str(j) for j in i] for i in data]

def part_one():
    data = get_data()
    closecount = {}
    maxdist = 500000
    # check to see if any particles get within 10 of 0,0,0
    for i in range(len(data)):
        pos, velo, acc = data[i]
        xp = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", pos).group(1))
        yp = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", pos).group(3))
        zp = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", pos).group(5))
        xv = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", velo).group(1))
        yv = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", velo).group(3))
        zv = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", velo).group(5))
        xa = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", acc).group(1))
        ya = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", acc).group(3))
        za = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", acc).group(5))
        closecount[i] = 0
        for j in range(5000):
            # print dist
            dist = abs(xp)+abs(yp)+abs(zp)
            if (dist <= maxdist):
                closecount[i] += 1
            xv += xa
            yv += ya
            zv += za
            xp += xv
            yp += yv
            zp += zv
    print max(closecount.iteritems(), key=operator.itemgetter(1))[0]

def positionstring(xp, yp, zp):
    return "%s%s%s" % (xp, yp, zp)

def part_two():
    data = get_data()
    positions = {}
    counter = 0
    # check to see if any particles get within 10 of 0,0,0
    for i in range(len(data)):
        pos, velo, acc = data[i]
        xp = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", pos).group(1))
        yp = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", pos).group(3))
        zp = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", pos).group(5))
        xv = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", velo).group(1))
        yv = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", velo).group(3))
        zv = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", velo).group(5))
        xa = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", acc).group(1))
        ya = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", acc).group(3))
        za = int(re.search(r"<((-)?\d+),((-)?\d+),((-)?\d+)>", acc).group(5))
        for j in range(5000):
            posStr = positionstring(xp, yp, zp) 
            if posStr in positions and positions[posStr][0] == j:
                # Found a collision so break
                counter += 1
                break
            else:
                positions[posStr] = [j, i] 
            xv += xa
            yv += ya
            zv += za
            xp += xv
            yp += yv
            zp += zv
    print 1000-counter
if __name__ == "__main__":
    # part_one()
    part_two()
