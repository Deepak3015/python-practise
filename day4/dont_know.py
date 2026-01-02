# def user_input():
#     n = int(input("Enter How many number you want you wants to add:"))
#     result = 0
#     for i in range (n):
#         number1 = int(input(f"Enter you {i+1} number:"))
#         result += number1
#     return result

# number  =user_input()

# print(f"The Result of your Operation is :{number}")


# def log_creator():
#     log = input("Enter your log here :")
#     with open("Log.txt","a") as file:
#         file.write(log +"\n")
#     print("Log Written succesfull")

# log_creator()

# Numbers =[]

# def add_args(*args):
#     dekh = 0
#     for number in args:
#         dekh += number
#     return dekh


# while(True):
#     number = input("Enter your Each Number gap by gap and right done after complete entering:")
#     if number.lower() =="done":
#         break
#     parts = number.split()
#     for p in parts :
#         if p.isdigit():
#             Numbers.append(int(p))
#         else:
#             print(f"Invalid_number:{p}")




# result = add_args(*Numbers)
# print(result)
# Numbers = []

# def add_args(*args):
#     total = 0
#     for number in args:
#         total += number
#     return total

# while True:
#     user_input = input(
#         "Enter numbers separated by space (type 'done' to finish): "
#     )

#     if user_input.lower() == "done":
#         break

#     stop = False

#     parts = user_input.split()   # 🔥 THIS IS THE KEY LINE

#     for p in parts:
#         if p.lower() == "done":
#             stop = True
#             break
#         elif p.isdigit():
#             Numbers.append(int(p))
#         else:
#             print(f"Ignored invalid input: {p}")
#     if stop:
#         break

# result = add_args(*Numbers)
# print("Sum =", result)

def logs(**kwargs):
    with open("log.txt" , "a") as file:
        for key ,value in kwargs.items():
            file.write(f"{key}:{value}\n")
        file.write("-" * 20 +"\n")

status = input("Enter status:")
Code = input("Enter Code:")
Message = input("Enter Message:")



log_dict = {
    "status":status,
    "code":Code,
    "Message":Message
}

logs(**log_dict)