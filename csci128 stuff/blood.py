# Roman Rodriguez
# CSCI-128 Section J
# Assessment 3
# References: no one
# Time: 30 minutes

# User input
primaryCurrent = input("MAIN> ")
backupCurrent = input("BACKUP> ")
typeReq = input("TYPE> ")
amountReq = int(input("AMOUNT> "))

# List things
primLst = primaryCurrent.split()
backLst = backupCurrent.split()
typeIndPrim = primLst.index(typeReq)
amtIndPrim = typeIndPrim + 1
typeIndBack = backLst.index(typeReq)
amtIndBack = typeIndBack + 1

# Print print printprintprntrinptprtirtrpnitptrpitp
if amountReq > int(primLst[amtIndPrim]) + int(backLst[amtIndPrim]):
    print("OUTPUT Error: Amount requested exceeds reserves")
elif amountReq < int(primLst[amtIndPrim]):
    print(f"OUTPUT Main Level: {int(primLst[amtIndPrim]) - amountReq}")
    print(f"OUTPUT Backup Level: {backLst[amtIndBack]}")
else:
    print("OUTPUT Warning: Main reserve depleted")
    print(f"OUTPUT Main Level: 0")
    amountReq -= int(primLst[amtIndPrim])
    if amountReq < int(backLst[amtIndBack]):
        print(f"OUTPUT Backup Level: {int(backLst[amtIndBack]) - amountReq}")
    else:
        print("OUTPUT Warning: Backup reserve depleted")
        print(f"OUTPUT Backup Level: 0")
