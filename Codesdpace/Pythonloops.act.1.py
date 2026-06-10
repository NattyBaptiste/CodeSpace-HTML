# Initialize the first two Fibonacci numbers
a = 0
b = 1

# Print Fibonacci numbers from 0 to 50
while a <= 50:
    print(a, end=" ")

    # Calculate the next Fibonacci number
    next_num = a + b

    # Update the values for the next iteration
    a = b
    b = next_num