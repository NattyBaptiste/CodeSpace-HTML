# Function to display the content of the list
def show_list(lst):
    # Print the list as it is
    print("The content of the list is:", lst)

# Function to find the maximum value in the list
def find_max(lst):
    # Use built-in max() function to get the largest value
    return max(lst)

# Sample list
numbers = [10, 2, 3, 4, 7]

# Call function to show list content
show_list(numbers)

# Call function to find and display max value
print("The max value in the list:", find_max(numbers))