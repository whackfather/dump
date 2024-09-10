# Roman Rodriguez
# CSCI-128 Section J
# Assessment 2
# References: No One
# Time: 30 Minutes

# User input
metal = input("METAL> ")
prices = input("PRICES> ")
densities = input("DENSITIES> ")
denIndicies = input("DENSITY_INDICES> ")
resist = input("RESISTS> ")

# Calculating metal weight
volume = 3.1415 * (0.5 ** 2) * (100 * 63360)
indexLst = denIndicies.split()
metalDen = float(densities[int(indexLst[0]):(int(indexLst[1]) + 1)])
weight = volume * metalDen

# Parsing out metal price
priceLst = prices.split()
metalPrice = float(priceLst[priceLst.index(metal) + 1])
costTotal = metalPrice * weight

# Resistivity magic
metalIndex = resist.index(metal)
resIndex = metalIndex + len(metal)
resMetal = float(resist[int(resIndex):int(resIndex + 4)])
crossSec = 3.1415 * (0.5 ** 2)
length = 63360 * 100
resistivity = (length / crossSec) * resMetal

# Printing outputs
print(f"OUTPUT {metal} Weight {weight:.3f}")
print(f"OUTPUT {metal} Price {costTotal:.3f}")
print(f"OUTPUT {metal} Resistivity {resistivity:.3f}")
