# Primitive data types - Strings, Integer, Float, Boolean
# num_char = len(input("What is your name?\n"))
# print(f'Your name has {num_char} characters.')

# type casting
# str(num_char) - converts to string
# type(num_char) - shows data type
# float(num_char) - turns into float

# Math operations - +, -, *, /
# ** - exponent, ex 2 ** 3 = 8
# division always creates float
# follows order of operations - PEMDAS

# BMI Calculator - weight/height squared
# weight = input('Enter your weight in kg:\n')
# height = input('Enter your height in m: \n')
# bmi = round(int(weight) / float(height) ** 2)
# round(8 / 3, 2) - rounds to 2 decimal places
# round(2.6666666, 2) - 2.67
# floor - (8 // 3) - output is 2, basically chops of anything after decimal
# print(f'Your BMI is {bmi} what does that mean? Who cares.')

# -=, +=, /=, *=
# score = 0
# score += 1
# print(score) # 1

# Time left exercise
# age = input('Enter your age:\n')
# months_left = (90 * 12) - (int(age) * 12)
# weeks_left = (90 * 52) - (int(age) * 52)
# days_left = (90 * 365) - (int(age) * 365)

# print("Here's how long you have left to live in different measurements (if you live to 90), have a nice day.")
# print(f"Months: {months_left}")
# print(f"Weeks: {weeks_left}")
# print(f"Days: {days_left}")

# Project - Tip Calculator
total = float(input("What was the total bill?\n"))
tip = float(input("What percentage would you like to tip?\n")) / 100
total_with_tip = (total * tip) + total
num_people = int(input("How many people are splitting the bill?\n"))
total_for_each = round(total_with_tip / num_people, 2)
print(f"Each person should pay: ${total_for_each}")




