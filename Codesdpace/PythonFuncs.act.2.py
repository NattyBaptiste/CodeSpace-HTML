# Function to calculate factorial of a non-negative integer
def factorial(n):
    # Check if the number is negative
    if n < 0:
        return "Factorial is not defined for negative numbers"

    # Initialize result as 1 (since 0! = 1)
    result = 1

    # Multiply numbers from 1 to n
    for i in range(1, n + 1):
        result *= i

    # Return the final factorial value
    return result


# Example usage
number = int(input("Enter a number: "))

# Call the function and display the result
print("Factorial is:", factorial(number))