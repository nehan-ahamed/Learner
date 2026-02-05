q_to_user= input('What type of calculation would you like to do? (add|+ , subtract|- , multiply|* , divide|/): ').lower()
if q_to_user == 'add' or q_to_user == '+':
    no1 = float(input('Enter the first number: '))
    no2 = float(input('Enter the second number: '))
    total = no1 + no2
    while True:
        no3 = input('Enter more number? (type done to calculate): ')
        if no3 == 'done':
            break
        total += float(no3)
    print(f'The total is: {total}')
elif q_to_user == 'subtract' or q_to_user == '-':
    no1 = float(input('Enter the first number: '))
    no2 = float(input('Enter the second number: '))
    total = no1 - no2
    while True:
        no3 = input('Enter more number? (type done to calculate): ')
        if no3 == 'done':
            break
        total -= float(no3)
    print(f'The total is: {total}')
elif q_to_user == 'multiply' or q_to_user == '*':
    no1 = float(input('Enter the first number: '))
    no2 = float(input('Enter the second number: '))
    total = no1 * no2
    while True:
        no3 = input('Enter more number? (type done to calculate): ')
        if no3 == 'done':
            break
        total *= float(no3)
    print(f'The total is: {total}')
elif q_to_user == 'divide' or q_to_user == '/':
    no1 = float(input('Enter the first number: '))
    no2 = float(input('Enter the second number: '))
    if no2 == 0:
        print('You cannot divide by zero')
    else:
        total = no1 / no2
        while True:
            no3 = input('Enter more number? (type done to calculate): ')
            if no3 == 'done':
                break
            elif float(no3) == 0:
                print('You cannot divide by zero')
                continue
            total /= float(no3)
        print(f'The total is: {total}')
else:
    print('Invalid input please try again')
