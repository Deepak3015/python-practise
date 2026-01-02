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

result_config = configparser.ConfigParser()

for student_id,books in student_details.items():
    total_cost = 0
    for book in books:
        total_cost += int(book_config["BOOKS"][book])
    result_config[f"Student_{student_id}"] = {"total_Cost":total_cost}
    
 
with open("/home/depliii/Desktop/GitHub/python-practise/day7/book_price.ini" ,"w") as  file:
    result_config.write(file)

print("Student book cost calculated successfully.")
