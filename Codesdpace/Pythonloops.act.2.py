# Input a number from the user
number = int(input("Input a number: "))

# Loop from 1 to 10 to generate the multiplication table
for i in range(1, 11):
    # Print the multiplication result
    print(f"{number} x {i} = {number * i}")