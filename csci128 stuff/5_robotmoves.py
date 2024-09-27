# Roman Rodriguez
# CSCI-128 Section J
# Assessment 5
# References: no one
# Time: 30 minutes

from math import sqrt

loop = True
batt = int(input("BATTERY> "))
heat = int(input("HEAT> "))
if heat >= 125 or batt <= 10:
    print(f"OUTPUT 0")
    print(f"OUTPUT 0.00 0.00")
    print(f"OUTPUT {int(heat // 1)}")
    print(f"OUTPUT {int(batt // 1)}")
    loop = False
old_x = 0
old_y = 0
moves = 0

while loop:
    coord = input("COORD> ")
    if coord == "DONE":
        print(f"OUTPUT {moves}")
        print(f"OUTPUT {old_x:.2f} {old_y:.2f}")
        print(f"OUTPUT {int(heat // 1)}")
        print(f"OUTPUT {int(batt // 1)}")
        break
    crdLst = coord.split()
    crdX = float(crdLst[0])
    crdY = float(crdLst[1])
    distMoved = sqrt(((int(crdX) - old_x) ** 2) + ((int(crdY) - old_y) ** 2))
    battExp = distMoved // 2
    batt -= battExp
    heatGen = battExp * 5
    heat += heatGen
    moves += 1
    print(f"OUTPUT {distMoved:.2f} {int(batt // 1)}")
    if heat >= 125 or batt <= 10:
        print(f"OUTPUT {moves}")
        print(f"OUTPUT {crdX:.2f} {crdY:.2f}")
        print(f"OUTPUT {int(heat // 1)}")
        print(f"OUTPUT {int(batt // 1)}")
        break
    old_x = int(crdX)
    old_y = int(crdY)
