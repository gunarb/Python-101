#######################################
# Functions with parameters
#######################################

# Define a function that receives a first name and a last name as parameters
def greet(first_name, last_name):
    # Use the parameter values to create a personalized greeting
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard!")


# Call the function and pass two arguments in the expected order
greet("Gunnar", "Bolanos")


#######################################
# Functions with a variable number of arguments
#######################################

# The asterisk collects all positional arguments into a tuple named numbers
def multiply(*numbers):
    # Start at 1 because multiplying a number by 1 does not change its value
    total = 1

    # Multiply the running total by each number in the tuple
    for number in numbers:
        total *= number

    # Send the final result back to the caller
    return total


# Call multiply with four arguments and print the returned result
print(multiply(2, 3, 4, 5))
