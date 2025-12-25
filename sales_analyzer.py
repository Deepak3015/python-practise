sales_data = [
    {"day": "Tuesday", "Amount": 1500},
    {"day": "Wednesday", "Amount": 800},
    {"day": "Thursday", "Amount": 2000},
    {"day": "Friday", "Amount": 1750}
]

total_sales = 0
low_sales = sales_data[0]
high_sales = sales_data[0]

for record in sales_data:
    amount = record["Amount"]
    total_sales += amount

    if amount > high_sales["Amount"]:
        high_sales = record

    if amount < low_sales["Amount"]:
        low_sales = record

average_sales = total_sales / len(sales_data)

print("----------------Sales Report----------------")
print("Total Sale:", total_sales)
print("Average Sales:", average_sales)
print("High sale:", high_sales["day"], high_sales["Amount"])
print("Low sale:", low_sales["day"], low_sales["Amount"])
