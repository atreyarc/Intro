from datetime import datetime

#function to print current date and time
def print_time(task_name):
    print(f'task {task_name} completed')
    print(datetime.now())
    print()

first_name = 'atreya'
print_time('first name print')

for x in range (0,10):
    print(x)
print_time('for loop execution')