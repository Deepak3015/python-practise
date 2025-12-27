def read_raw_data(filename):
    with open("raw_sales.csv","r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines[1:]]

def clean_data(raw):
    clean_data=[]
    for data in raw:
        if "," not in data:
            continue
        day,amount = data.split(",")
        try:
            amount = int(amount)
            if amount < 0:
                continue
        except:
            continue
        clean_data.append({"day":day,"amount":amount})
    return clean_data

def write_clean_data(file_name,clean_data):
    with open(file_name,"w") as file:
        file.write("day.amount\n")
    for record in clean_data:
        file.write(f"{record["day"]},{record["amount"]}\n")

def generate_report(clean_data):
    total = 0
    high = clean_data[0]
    low = clean_data[0]

    for record in clean_data:
        amount = record["amount"]
        total += amount

        if amount > high["amount"]:
            high = record
        if amount < low["amount"]:
            low = record

    average = total / len(clean_data)

    print("----- SALES REPORT -----")
    print("Total:", total)
    print("Average:", average)
    print("Highest:", high["day"], "-", high["amount"])
    print("Lowest:", low["day"], "-", low["amount"])






