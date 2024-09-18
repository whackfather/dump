# Roman Rodriguez
# CSCI-128 Section J
# Assessment 4
# References: no one
# Time: 25 minutes

gate = input("GATE> ")
inp1 = int(input("INP1> "))
inp2 = int(input("INP2> "))
validgates = ["AND", "OR", "NAND", "NOR", "XOR", "XNOR"]

if gate not in validgates:
    print(f"OUTPUT Invalid Gate {gate}")
elif inp1 != 0 and inp1 != 1:
    print(f"OUTPUT Invalid Input {inp1}")
elif inp2 != 0 and inp2 != 1:
    print(f"OUTPUT Invalid Input {inp2}")
else:
    if gate == "AND":
        if inp1 == 1 and inp2 == 1:
            print("OUTPUT True")
        else:
            print("OUTPUT False")
    elif gate == "OR":
        if inp1 == 1 or inp2 == 1:
            print("OUTPUT True")
        else:
            print("OUTPUT False")
    elif gate == "NAND":
        if inp1 == 1 and inp2 == 1:
            print("OUTPUT False")
        else:
            print("OUTPUT True")
    elif gate == "NOR":
        if inp1 == 1 or inp2 == 1:
            print("OUTPUT False")
        else:
            print("OUTPUT True")
    elif gate == "XOR":
        if inp1 == 1 and inp2 == 1:
            print("OUTPUT False")
        elif inp1 == 1 or inp2 == 1:
            print("OUTPUT True")
        else:
            print("OUTPUT False")
    elif gate == "XNOR":
        if inp1 == 1 and inp2 == 1:
            print("OUTPUT True")
        elif inp1 == 1 or inp2 == 1:
            print("OUTPUT False")
        else:
            print("OUTPUT True")
