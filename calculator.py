from art import logo
from replit import clear


#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2


#Get Operator
def operator(list_operation):
    for operator in list_operation:
        print(operator)

    while True:
        try:
            operator = input("Pick an operation: ")
            if operator == "+" or operator == "-" or operator == "/" or operator == "*":
                return operator
                break
            else:
                print("You should pick a valid operator")
        except ValueError:
            print("Invalid input. Please enter a valid operator.")


#Final Result


def final_result(firstNum, operation, secondNum):
    result = list_operation[operation](firstNum, secondNum)
    print(f"{firstNum} {operation} {secondNum} = {result}")

    return result


list_operation = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    from_zero = True

    print(logo)
    while True:
        try:
            num1 = float(input("What is the first number?: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while from_zero:

        my_operator = operator(list_operation)

        while True:
            try:
                num2 = float(input("What is the next number?: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        result = final_result(num1, my_operator, num2)

        if input(
                f"Type 'y' to continue with {result}, or type 'n' to start a new calculation? "
        ).lower() == "y":
            num1 = result
        else:
            from_zero = False
            clear()
            calculator()


calculator()
