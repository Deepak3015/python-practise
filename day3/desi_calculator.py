def calculator():
    result = None

    while True:
        if result is None:
            num1 = float(input("Enter you first Number:"))
        else:
            num1 = result
        

        op = input("Choose your operator +,-,*,/:---")
        num2 = float(input("Enter your Second Number:"))

        if op == "+":
            result = num1+num2
        elif op =="-":
            result = num1-num2
        elif op =="*":
            result = num1*num2
        elif op =="/":
            if num2 != 0:
                result = num1/num2
            else:
                continue
        else:
            print("Invalid Operator!!!!!!")
            continue
        print("Result:",result)
        choice = input("Wants to 'C'ontine this calculation or wants a 'N'ew Calculation or wants to 'E'xit the program:--").lower()
        if choice == "n":
            result = None
        elif choice == "e":
            print("Exiting the program..............")
            break


calculator()
