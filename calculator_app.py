# Task 1

input_type = input("What kind of operation would you like to make? (addition, subtraction, multiplication, or division)")
first_number = int(input("What is the first number? "))
second_number = int(input("What is the second number? "))

def addition(first_number, second_number):
    calculate_addition = first_number + second_number
    return calculate_addition

def subtraction(first_number, second_number):
    calculate_subtraction = first_number - second_number
    return calculate_subtraction

def multiplication(first_number, second_number):
    calculate_multiplication = first_number * second_number
    return calculate_multiplication

def division(first_number, second_number):
    calculate_division = first_number / second_number if second_number != 0 else 0
    return calculate_division

if input_type == "addition":
    x = addition(first_number, second_number)
    print("Your total is: ", x)
elif input_type == "subtraction":
    x = subtraction(first_number, second_number)
    print("Your total is: ", x)
elif input_type == "multiplication":
    x = multiplication(first_number, second_number)
    print("Your total is: ", x)
elif input_type == "division":
    x = division(first_number, second_number)
    print("Your total is: ", x)
else:
    print("Please check operation spelling! Try again!")