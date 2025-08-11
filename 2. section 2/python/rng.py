from random import randint

min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))

if max_value < min_value:
    print("Error: Maximum value must be greater than or equal to minimum value.")
else:
    random_number = randint(min_value, max_value)
    print(random_number)