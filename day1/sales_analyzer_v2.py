sales_data = []

with open("sales_data.csv","r") as file:
    lines = file.readlines()
for line in lines[1:]:
    day,amount = line.strip().split(",")

    record = {

        "day":day,
        "amount":int(amount)
    }

    sales_data.append(record)

def analyze_data(data):
    total_sales = 0
    high_sales = data[0]
    low_sales = data[0]

    for record in data:
        amount=record["amount"]
        total_sales += amount
        if amount > high_sales["amount"]:
            high_sales = record
        if amount < low_sales["amount"]:
            low_sales = record
    avergae_sales = total_sales/len(data)
    return avergae_sales, total_sales,high_sales,low_sales

avg, total, high, low = analyze_data(sales_data)
print("----- SALES REPORT (FROM CSV) -----")
print("Total Sales:", total)
print("Average Sales:", avg)
print("Highest Sale:", high["day"], "-", high["amount"])
print("Lowest Sale:", low["day"], "-", low["amount"])

    