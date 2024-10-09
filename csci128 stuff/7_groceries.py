# Roman Rodriguez
# CSCI-128 Section J
# Assessment 7
# References: no one
# Time: 30 minutes

def process_inventory(items, current_inventory, inventory_delta) -> None:
    for i in range(len(current_inventory)):
        current_inventory[i] += inventory_delta[i]
        if current_inventory[i] < 0: current_inventory[i] = 0

def process_sale(items, current_inventory, item, quantity) -> str:
    itemInd = items.index(item)
    sold = 0
    if quantity > current_inventory[itemInd]: sold = current_inventory[itemInd]
    else: sold = quantity
    current_inventory[itemInd] -= quantity
    if current_inventory[itemInd] < 0: current_inventory[itemInd] = 0
    return f"{item} {sold}"

def generate_eod_report(items, closing_inventory, prices, running_sales_report) -> list:
    eodReport = []
    newSalesReport = []
    for i in running_sales_report:
        i = i.split()
        for j in i:
            newSalesReport.append(j)
    print(newSalesReport)
    for i in range(len(items)):
        if items[i] in newSalesReport:
            soldAmt = float(newSalesReport[newSalesReport.index(items[i]) + 1])
            soldPrice = soldAmt * prices[i]
        else:
            soldAmt = 0
            soldPrice = 0.00
        itemOut = f"{items[i]}: Inventory: {closing_inventory[i]} ${prices[i]*closing_inventory[i]:.2f} Sold: {soldAmt:.0f} ${soldPrice:.2f}"
        eodReport.append(itemOut)
    
    return eodReport
