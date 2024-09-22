#Prompt for user input
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

#Asking the type of operation
operation = input("Choose the operation (+, -, *, /):")

#Performing the calculation using Match Case
match operation:
    case "+":
        result = num1 + num2
        print("The result is", result, ".")
    case "-":
        result = num1 - num2
        print("The result is", result, ".")
    case "*":
        result = num1 * num2
        print("The result is", result, ".")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print("The result is", result, ".")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please choose +, -, *, or /.")