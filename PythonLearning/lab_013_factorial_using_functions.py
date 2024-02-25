def factorial_no(number):
    if number < 0:
        return "Invalid input. Please provide a non-negative integer."
    elif number == 0:
        return 1
    else:
        factorial_result = 1
        #for i in range(1, number + 1):
         #   factorial_result *= i
        for i in range(number):
            factorial_result = number * factorial_result
            number = number - 1
        return factorial_result

# Example usage:
num = 5
result = factorial_no(num)
print(f"The factorial of {num} is: {result}")




