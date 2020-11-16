num1 = input('first number: ')
operator = input('operation: ')
num2 = input('second number:')
if(num1.isnumeric() and num2.isnumeric()):
    if(operator == '+'):
        print('Sum of',num1,'and', num2, 'is', int(num1)+int(num2))
    elif(operator == '-'):
        print('Substraction of',num1,'and', num2, 'is', int(num1)-int(num2))
    elif(operator == '*'):
        print('Multiplication of',num1,'and', num2, 'is', int(num1)*int(num2))
    elif(operator == '/'):
        print('Quotient of',num1,'and', num2, 'is', int(num1)/int(num2))
    elif(operator == '^'):
        print('Exponent of',num1,'and', num2, 'is', int(num1)^int(num2))
    elif(operator == '%'):
        print('Modulus of',num1,'and', num2, 'is', int(num1)%int(num2))
    else:
        print('Operator not recognized')
else:
    print('Please enter only numbers.')
