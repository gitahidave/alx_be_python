#Prompting user for pattern size
length = int(input("Enter the size of the pattern:"))

#Drawing the pattern
row = 0
while row < length:
    # Use a for loop to print asterisks side by side for each column in the row
    for col in range(length):
        print("*", end="")
    # Print a newline character after each row
    print()
    # Move to the next row
    row += 1