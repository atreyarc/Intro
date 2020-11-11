#this function returns the first letter of passed input strings
def get_initial(name):
    initial =  name[0:1]
    return initial

first_name=input('Enter your first name: ')

middle_name=input('Enter your middle name: ')

last_name=input('Enter your last name: ')

print(get_initials(first_name)+get_initials(middle_name)+get_initials(last_name))