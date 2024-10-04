# Roman Rodriguez
# CSCI-128 Section J
# Assessment 5
# References: no one
# Time: 15 minutes

years = int(input("YEARS> "))
rate = float(input("INTEREST> "))
cont = float(input("CONTRIBUTION> "))
type = int(input("METHOD> "))
total = 0

if type == 1:
    for i in range(years):
        total += cont * 12
        newtot = (rate + 1) * total
        total = newtot
    print(f"OUTPUT {total:.2f}")
elif type == 2:
    for i in range(years * 12):
        total += cont
        newtot = (rate + 1) * total
        total = newtot
    print(f"OUTPUT {total:.2f}")
elif type == 3:
    for i in range(years * 360):
        if i % 30 == 0:
            total += cont
        newtot = (rate + 1) * total
        total = newtot
    print(f"OUTPUT {total:.2f}")
