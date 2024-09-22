#Prompting user for a number
number = int(input("Enter a number to see its multiplication table:"))

#Generate and print the multiplication table
print("Multiplication for", number, ":")
for i in range(1, 11):
    result = number * i
    print(number, "*", i,"=", result)