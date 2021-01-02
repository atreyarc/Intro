import random
number = random.randint(1,5)
count = 0
guess = 0
while int(guess) != number:
    count +=1
    guess = input('Guess a number between 1 and 5 or press \'q\' to quit: ')
    
    if guess.strip() =='':
        continue
    if guess.strip()=='q':
        break
    
    print('Entered guess #'+ str(count) + ': ' + str(guess))
    
    if not (guess.isnumeric()):
        print('Numbers only please')
        guess = 0
        continue
    
    if(int(guess)<number):
        print('Your guess is too low. Try again.')
    elif (int(guess)>number):
        print('Your aguess is too high. Try again.')
    else:
        print(f'You guessed it in {count} tries!')