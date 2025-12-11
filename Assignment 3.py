## Task 1
def factorial(number):
    if number < 0:
        return "Factorial is not defined or negative numbers."
    elif number == 0:
        return 1
    else:
        fact = 1
        for i in range(1, number + 1):
            fact *= i
        return fact

number=input("Enter a number : ")
result=factorial(int(number))
print(f"The factorial of {number} is {result} ")

## Task 2

import math

number =int(input("Enter a number : "))

a=math.sqrt(number)
b=math.log(number)
c=math.sin(number)

print(f"Square Root: {a}")
print(f"Natural Log : {b}")
print(f"Sine : {c}")




