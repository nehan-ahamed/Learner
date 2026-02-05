# This is my first python
#print("hello world")


#Variable = A container for a value (1.string, 2.integer, 3.float, 4.boolean)
#           A variable behaves as if it was the value it contains

#print(first_name)

#Use f string when typing a sentence with a variable

#Strings (they are a series of characters)
#first_name = 'Nehan'
#food = 'pizza'
#email = 'nehanmms7@gmail.com'

#print(f'hello {first_name}')
#print(f'Do you like {food}')
#print(f'Your email is: {email}')

#Integers (they are numbers), integers should not be within "" since then they would count as strings
# integers are whole numbers
#Age = 18
#Quantity = 5
#number_of_students = 30
#print(f'Your age is {Age}')
#print(f'You are buying {Quantity} {food}s')
#print(f'Your class has {number_of_students} students')

# Floats (these contain a decimal place)
#price = 10.99
#gpa = 4.3
#distance = 3.5
#print(f'The price of one {food} is ${price}')
#print(f'Your gpa is {gpa}')
#print(f'You ran {distance} km')

# Boolean (this is either true or false)
#is_student = True
#print(f'Are you a student? : {is_student}')

#if is_student:
 #   print('You are a student')
#else:
 #   print('You are not a student')



# Typecasting = the process of converting a variable form one data type to another str(), int(), float(), bool()

#name = 'Nehan'
#age = 18
#gpa = 4.3
#is_studnet = True

#age = str(age)
#print(age)



# input() =  A function that prompts the user to enter data
#            Return the entered data as string

#name = input('What is your name?: ')
#age = int(input('How old are you?: '))
#age = int(age)
#age = age + 1
#print(f'Hello {name}!')
#print('Happy birthday')
#print(f'You are {age} years old.')


# Exercise 1: Calculate the area of a rectangle
#length = float(input("What is the length of the rectangle?: "))
#width = float(input("What is the width of the rectangle?: "))
#print(f'The Area of the rectangle is: {length * width}cm^2')


# Exercise 2: Create a Shopping cart program

#item = input('What is your item?: ')
#price = float(input(f'What is the price of each {item}?: $'))
#quantity = int(input(f'How many {item}/s would you like?: '))
#print(f'The total price of your {item}/s is ${price * quantity}')


# Madlibs game, it is a word game where you create a story

#adjective1 = input('Enter adjective: ')
#adjective2 = input('Enter adjective 2: ')
#adjective3 = input('Enter adjective 3: ')
#noun1 = input('Enter noun: ')
#verb1 = input('Enter verb: ')

#print(f'Today I went to a {adjective1} zoo')
#print(f'In an exhibit, I saw a {noun1}')
#print(f'{noun1} was {adjective2} and {verb1}')
#print(f'I was {adjective3}')


# Maths

#Money = 100
# 1. Addition
#Money = Money + 15
#Money += 15
#print(Money)

# 2. Subtraction
#Money = Money - 15
#Money -= 15
#print(Money)

# 3. Multiplication
#Money *= 12
#print(Money)

# 4. Division
#Money /= 2
#print(Money)

# 5. Exponent
#Money **= 3
#print(Money)

# 6. Modulus (it shows the reminder of a division)
#Money = Money % 7
#Money %= 7
#print(Money)


#x = 2.393
#y = -329
#z = 0.123

# 7. Rounding the no.
#result = round(x)
#print(result)

# 8. Absolute (it is the distance form 0)
#result = abs(y)
#print(result)

# 9. Power
#result = pow(y, 3)
#print(result)

# 10. Max value between no.
#result = max(x, y, z)
#print(result)

# 11. Min value between no.
#result = min(x, y, z)
#print(result)

#import math
# need to write import math in order for these to work

# 12. Value of Pi
#print(math.pi)

# 13. Value of exponential
#print(math.e)

# 14. Square root of a number
#result = math.sqrt(256)

# 15. Ceil (it is rounding UP a number)
#result = math.ceil(3.219)

# 16. Floor (it is rounding DOWN a number)
#result = math.floor(3.919)
#print(result)

# 17. % (it will give the reminder of a division)
#print(22%5)

# Calculating the circumference of a circle
#import math
#Radius = float(input('What is the radius of the circle?: '))
#pi = math.pi
#print(f'The circumference of the circle with radius {Radius} is {2*pi*Radius} ')

# Calculating the Area of a semi-circle
#import math
#PI = math.pi
#Radius = float(input('What is the radius of the circle?: '))
#Radius **= 2
#print(f'The Area of the Semi-Circle is {(PI*Radius)/2}')

# Calculating the hypotunus of a right angle triangle
#import math
#length_a = float(input('What is the length of A: '))
#length_b = float(input('What is the length of B: '))
#length_a **= 2
#length_b **= 2
#length_c = math.sqrt( length_a + length_b)
#print(f'The hypotunus of your triangle is {round(length_c,2)}')



# if statements = do some code only IF some condition is True
#                 Else do something else and use elif for other options

#age = int(input("How old are you?: "))
#if age >= 100 :
#    print('Please enter a valid age.')
#elif age <= 0 :
#    print('Please enter a valid age.')
#elif age >= 18 :
#    print('You are eligible for applying.')
#else :
#    print('You are not eligible for applying')

#name = input('What is your name?: ')
#if name == '' :
#    print('Please enter a name.')
#else :
#   print(f'Hello {name}')

#Use of boolean in if statements

#online = False
#if online :
#    print('The user is online')
#else:
#    print('The user is offline')




#Try and except (non BroCode)

#user= input('Please input any variable: ')
#try:
#  value= int(user)
#except ValueError:
#  try:
#    value= float(user)
#  except ValueError:
#    value= user
#print(type(value))

#TO give a certian decimal place use :.2f the 2 represents no. of decimal places
















