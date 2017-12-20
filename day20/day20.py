#!/usr/bin/python
import re, operator
from itertools import chain
def get_data():
    with open('input.txt', 'r') as f:
        data = [s.strip().split() for s in f.readlines()]
    return [[str(j) for j in i] for i in data]

def part_one():
    data = get_data()
    partDist = {}
    t = 1000
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
        distX = xp + (xv*t) + (0.5)*(xa)*(t ** 2)
        distY = yp + (yv*t) + (0.5)*(ya)*(t ** 2)
        distZ = zp + (zv*t) + (0.5)*(za)*(t ** 2)
        realDist = abs(distX) + abs(distY) + abs(distZ)
        partDist[i] = realDist
    print min(partDist.iteritems(), key=operator.itemgetter(1))[0]

def positionstring(xp, yp, zp):
    return "%s%s%s" % (xp, yp, zp)

def part_two():
    data = get_data()
    positions = {}
    dupPos = {}
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
        for j in range(1000):
            posStr = positionstring(xp, yp, zp) 
            if posStr in positions and positions[posStr][0] == j:
                # Found a collision so break
                # This does not account for the original particle that moved to this position
                if posStr in dupPos:
                    dupPos[posStr] += 1
                else:
                    dupPos[posStr] = 2
                break
            else:
                positions[posStr] = [j, i] 
            xv += xa
            yv += ya
            zv += za
            xp += xv
            yp += yv
            zp += zv
    for val in dupPos:
        counter += dupPos[val]
    print dupPos
    print len(data)-counter
if __name__ == "__main__":
    part_one()
    # part_two()
