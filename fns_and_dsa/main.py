from arithmetic_operations import perform_operation

def main():
    try:
        # Input numbers and operation from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()

        # Perform the operation
        result = perform_operation(num1, num2, operation)
        
        # Display the result
        print(f"The result is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
