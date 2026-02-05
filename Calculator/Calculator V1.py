# Creating A Calculator In Python

#1. Find what operation the user is trying to do ( addition/subtraction/multiplication/division)
#2. Tell the user to input the numbers
#3. Perform the operation

import math
pi = math.pi
numbers = float(input('Enter number: '))
operation = input('What operation would you like to perform? Please type one of the following: add/+, subtract/-, multiply/*, divide/: ').lower()
number2 = float(input('Enter number: '))
if operation == 'add':
    print(numbers + number2)
elif operation == 'subtract':
    print(numbers - number2)
elif operation =='multiply':
    print(numbers * number2)
elif operation =='divide':
    if number2 == 0:
        print('Cannot divide by zero')
    else:
     print(numbers / number2)
else:
    print('Invalid operation')