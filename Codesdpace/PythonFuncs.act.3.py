# Function to check whether a number is prime or not
def is_prime(n):
    # Negative numbers, 0 and 1 are not prime
    if n <= 1:
        return False

    # Check divisibility from 2 to n-1
    for i in range(2, n):
        # If divisible by any number, it is not prime
        if n % i == 0:
            return False

    # If no divisors found, it is prime
    return True

# Input a number from the user
number = int(input("Enter a number: "))

# Check and display result
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")