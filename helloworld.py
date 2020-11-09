fname = input("What is your name? ")
#print("this is a comment test")
print("hello", fname)
lname = input("What is your last name? ")
fullname = fname + " " + lname
print("Your full name is ", fullname)
fullname = fullname.lower() #makes all letters as lowercase and stores back to fullname.
print(fullname.capitalize()) #capitalizes only first letter
print(fullname.upper())
print(fullname.count('a')) #counts all instances of a particular string in full name. In this case - 'a'

#these are different ways to do string formatting. 
#Available only in py3+. Best and simplest way.
output = f'Hello, {fname} {lname} in py3+' 
print(output)

#this is in py2+. 
output = 'Hello, {} {} in py2+'.format(fname, lname) 
print(output)

#this is in py2+. This time with format indexing  
output = 'Hello, {1} {0} in py2+'.format(fname, lname) 
print(output)

#working with numbers
# + -> addition
# - -> subtraction
# * -> multiplication
# / -> division
# ** -> exponent

#type casting to str
days_in_feb = 28
print(str(days_in_feb) + " days in feb")

#input always takes input in string
first_num = input("Enter first number")
second_num = input("Enter second number")
print(int(first_num) ** float(second_num))
#this works because float and int can work together. However, int and string cannot work together. 

#working with dates
#to get current date and time we need to use the datetime
from datetime import datetime, timedelta

current_date = datetime.now()
#the now function returns the date time object. Let's convert that to string
print("Today is: " + str(current_date))

#You can use timedelta to add or remove days / weeks to a date
one_week= timedelta(weeks=1)
a_week_ago = current_date - one_week
print("last week was ", a_week_ago)

#formatting current date for only relevant data
print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))

#taking date inputs
birthday = input('When is your birthday (dd/mm/yyyy)?')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print('Week before birthday is: ', str(birthday_date-one_week))

#validating data input - try- except - finally
x = 42
y = 0

try:
    print (x/y)
except ZeroDivisionError as e:
    print('Not allowed to divide by zero')
    #the way to find the error name is by running the error creating code again. the terminal will give the name of the error.
else:
    print('Something else went wrong')
finally:
    print('This is our clean up code')

#Handling if else
price = input('how much did you pay?')
price = float(price)
if price >= 1.00 \
    or price >0.8:#multiple ORs can be tagged under IN statement
    tax=0.5
elif price <=0.5:
    tax = 0.7
else:
    tax = 0
print("Your tax is ", str(tax))

#collections
#lists
#allows any data type and mixture of data types
scores = []
scores.append(98) #add a new item
scores.append(99) #add a new item

print(scores)
print(scores[1])

names = ['abc', 'def']
print(len(names))
names.insert(1,'ghi')
print(names)
names.sort()
print(names)

#retrieving ranges in list
presenters = names[1:2]
print(presenters)
presenters = names[:2]
print(presenters)

#array
#only allows number datatypes.
from array import array
scores = array('d')
scores.append(97)
scores.append(98)

print(scores)
print(scores[1])

#dictionaries - with key value pair
person = {'first':'Chris'}
person['last']='Harris'
print(person)
print(person['first'])

human = {'first':'Susan'}
human['last']='Wolfe'
print(human)
print(human['first'])

#creating an array of dictionaries
people = []
people.append(person)
people.append(human)
people.append({
    'first':'Bill','last':'Gates'
})
print(people)

#Loops
#For + while loop combination
index = 0
while index < len(people)-1:
    print (people[index])
    index += 1