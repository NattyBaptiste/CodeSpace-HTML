# Input the first number from the user
first_number = int(input("Input first number: "))

# Input the second number from the user
second_number = int(input("Input second number: "))

# Input the third number from the user
third_number = int(input("Input third number: "))

# Check if all three numbers are equal
if first_number == second_number == third_number:
    print("All numbers are equal.")

# Check if all three numbers are different
elif first_number != second_number and first_number != third_number and second_number != third_number:
    print("All numbers are different.")

# Otherwise, neither all are equal nor all are different
else:
    print("Neither all are equal or different.")
    