farenheit = input ('enter farenheit value: ')

if(farenheit.isnumeric()):
    celsius = (int(farenheit) - 32)*5/9
    print(f'Value in celsius is: ',int(celsius))
    exit()
else:
    print('please enter correct data')
    exit()

