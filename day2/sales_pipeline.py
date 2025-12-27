raw_data = []

with open("raw_data.csv", "r") as file:
    lines = file.readlines()

for line in lines[1:]:
    raw_data.append(line.strip())


clean_data = []

for raw in raw_data:

    if "," not in raw:
        continue

    day, amount = raw.split(",")

    try:
        amount = int(amount)
        if amount < 0:
            continue
    except:
        continue

    clean_data.append({"day": day, "amount": amount})


with open("clean_data.csv", "w") as file:
    file.write("day,amount\n")
    for record in clean_data:
        file.write(f"{record['day']},{record['amount']}\n")


total = 0
high_sales = clean_data[0]
low_sales = clean_data[0]

for data in clean_data:
    amount = data["amount"]
    total += amount

    if amount > high_sales["amount"]:
        high_sales = data
    if amount < low_sales["amount"]:
        low_sales = data


average = total / len(clean_data)

print("----- CLEAN SALES REPORT -----")
print("Total:", total)
print("Average:", average)
print("Highest:", high_sales["day"], "-", high_sales["amount"])
print("Lowest:", low_sales["day"], "-", low_sales["amount"])
