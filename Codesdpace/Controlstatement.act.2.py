# Input the first number from the user
first_number = int(input("Input first number: "))

# Input the second number from the user
second_number = int(input("Input second number: "))

# Input the third number from the user
third_number = int(input("Input third number: "))

# Check if the numbers are in increasing order
if first_number < second_number < third_number:
    print("Increasing order.")

# Check if the numbers are in decreasing order
elif first_number > second_number > third_number:
    print("Decreasing order.")

# Otherwise, the numbers are neither increasing nor decreasing
else:
    print("Neither increasing or decreasing order.")