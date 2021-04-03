import math

def calculator():
    number_1 = int(input("Enter a number: "))
    number_2 = int(input("Enter a number: "))
    operators = "+, -, *, /, **"
    operator = input("Choose an operator from this list: {} ".format(operators))
    if operator not in operators:
        print("Invalid operator, choose again.", operator)
    elif operator == "+":
        print(number_1 + number_2)
    elif operator == "-":
        if number_1 > number_2:
            print(number_1 - number_2)
        else:
            print(number_2 - number_1)
    elif operator == "*":
        print(number_1 * number_2)
    elif operator == "/":
        if number_1 > number_2:
            print(math.floor(number_1 / number_2))
        else:
            print(math.floor(number_2 / number_1))
    elif operator == "**":
        print(number_1 ** number_2)

calculator()
