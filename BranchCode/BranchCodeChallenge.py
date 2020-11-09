#This program is a response to a challenge in https://docs.microsoft.com/en-us/learn/modules/python-if-elif-else/4-challenge

user_input = input('Would you like to continue? ')
if(user_input == 'y' or user_input == 'yes'):
    print("Continuing")
    print('Complete!')
elif (user_input == 'n' or user_input == 'no'):
    print('Exiting')
else:
    print('Please try again and respond with yes or no')