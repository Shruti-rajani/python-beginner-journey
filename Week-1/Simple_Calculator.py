def calculator():
    while True:
        try:
            num1 = float(input("Enter First Number: "))
            break
        except ValueError:
            print("Invalid input")

    operand = input("Enter Operand: ")
    while True:
            try:
                num2 = float(input("Enter Second Number: "))
                break
            except ValueError:
                print("Invalid input")
        
    if operand == "+":
        print(f"Sum = {num1 + num2}")
    elif operand == "-":
        print("Substarction = ", num1-num2)
    elif operand == "/":
        if num2 == 0:
            print("Cannot divided a number with a zero")
        else:
            print(f"Division = {num1 / num2}")
    elif operand == "*":
        print(f"Multiplication = {num1*num2}")
    else:
        print("Invalid Operand")
print("Simple Python Calculator")
calculator()
