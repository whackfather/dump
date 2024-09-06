# Nosecone Calculator
# UI and Error Catching
# v2.1
# Written by Roman Rodriguez

import nccalcs

valid_names = ["conic", "cn", "parabolic", "pb", "haack", "hs", "power", "ps", "ellipse", "ep", "ogive", "to"]
print("Welcome to the Nosecone Radius Calculator.")
print('Enter "help" for help, or "exit" to close program.')
print("Valid shape name entries:")
print(str(valid_names).replace("[", "").replace("]", "").replace("'", ""))

while True:
    shape = input("Enter shape name: ")
    if shape == "exit":
        print("Closing program.")
        exit(0)
    elif shape == "help":
        nccalcs.helpmenu()
    elif shape not in valid_names:
        print("PLEASE ENTER A VALID SHAPE NAME.")
    else:
        rad_o = input("Enter radius (INCHES ONLY): ")
        if rad_o == "exit":
            print("Closing program.")
            exit(0)
        elif rad_o == "help":
            nccalcs.helpmenu()
            rad_o = 1
            leave = True
        try:
            float(rad_o)
        except:
            print("PLEASE ENTER A VALID RADIUS.")
            leave = True
        if leave:
            leave = False
        else:
            rad_o = float(rad_o)
            lng_o = rad_o * 10
            length = 0
            nccalcs.calculate(shape, rad_o, lng_o, length)
