# Roman Rodriguez
# CSCI 128 - Section J
# Assessment 1
# References: no one
# Time: 45 minutes

# Setup
mineName = input("NAME> ")
goldPrice = input("PRICE> ")
print(f"\nOUTPUT Investment Planning Report of {mineName} Mine")
reclamation = 150000000

# Development cost (in USD)
land_bldgs = 145230000
mainEquip = 36200000
openingsDev = 209500000
infra = 80700000
dam = 48100000
misc = 28200000
investment = land_bldgs + mainEquip + openingsDev + infra + dam + misc
print("\nInital investment cost (USD):")
print(f"OUTPUT {investment}")

# Yearly operating cost (in USD)
excavation = 9000000
processing = 10000000
employees = 100000 * 150
others = 100000000
costYearly = excavation + processing + employees + others
print("\nYearly operation cost (USD):")
print(f"OUTPUT {costYearly}")

# Yearly Grams of Gold
refinedGold = 11000000 * 0.95  # grams
print("\nTotal yearly refined gold (grams):")
print(f"OUTPUT {int(refinedGold)}")

# Yearly Revenue
profitYearly = refinedGold * int(goldPrice) - costYearly
print("\nExpected yearly profit (USD):")
print(f"OUTPUT {int(profitYearly)}")

# Total Profit
totalGainz = 20 * profitYearly - investment - reclamation
print("\nExpected total profit over standard 20 year period (USD):")
print(f"OUTPUT {int(totalGainz)}")

print("\n\nReport calculation program written by Roman Rodriguez")
