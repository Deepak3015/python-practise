# def unique_name(filename):
#     try:
#         with open(filename,"r") as f:
#          content = f.read().strip()

#         if content == "":
#             raise Exception("File is empty")

#         names = content.split("\n")
#         unique_names = set(names)
#         for name in unique_names:
#          print(name)
    
#     except FileNotFoundError:
#         print("File not Found")
#     except Exception as e :
#        print(f"Error:{e}")
# unique_name("day7/names.txt")

import configparser

book_config = configparser.ConfigParser()
book_config.read("/home/depliii/Desktop/GitHub/python-practise/day7/book_price.ini")

student_details = {
    1: ["Math", "History"],
    2: ["Biology", "Chemistry", "History"],
    3: ["Science"]
}

for student_id,books in student_details.items():
    total_cost = 0
    for book in books:
        total_cost += int(book_config["BOOKS"][book])
    if len(books) >= 2:
        discount = total_cost * 0.10
    else:
        discount = 0

    final_cost = total_cost - discount

    # Save result in SAME ini file
    book_config[f"Student_{student_id}"] = {
        "books_bought": str(len(books)),
        "total_cost": str(total_cost),
        "discount": str(int(discount)),
        "final_cost": str(int(final_cost))
    }
    
 
with open("/home/depliii/Desktop/GitHub/python-practise/day7/book_price.ini" ,"w") as  file:
    book_config.write(file)

print("Student book cost calculated successfully.")
