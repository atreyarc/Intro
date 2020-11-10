""" medicine = 'Coughussin'
dosage = 5
duration = 4.5

instructions = '{} - Take {} ML by mouth every {} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{2} - Take {1} ML by mouth every {0} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneezergen', dosage = 10, duration = 6)

print(instructions) """
""" 
name = 'World'
message = f'Hello, {name}.' #The format() function is powerful and flexible. You can achieve the same functionality, with less typing, by using formatted string literals, also known as f-strings.
print(message)

count = 10
value = 3.14
message = f'Count to {count}.  Multiply by {value}.'
print(message) 

 """
""" 
width = 5
height = 10

print(f'The perimeter is {(2 * width) + (2 * height)} and the area is {width * height}.') """

value = 'hi'

print(f'.{value:<25}.')#A format specifier uses a colon symbol (:) after the variable name, to specify how that value should be formatted.
print(f'.{value:>25}.')
print(f'.{value:^25}.')
print(f'.{value:-^25}.')