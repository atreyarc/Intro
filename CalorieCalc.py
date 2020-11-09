#import date time
from datetime import datetime, timedelta

current_date =  input('Today\'s date (dd/mm/yyyy):\n')
breakfast_calories = int(input('Breakfast calories: \n'))
lunch_calories = int(input('lunch calories: \n'))
dinner_calories = int(input('dinner calories: \n'))
snack_calories = int(input('snack calories: \n'))

print('Calorie content for ', current_date," : ", breakfast_calories+lunch_calories+dinner_calories+snack_calories)
