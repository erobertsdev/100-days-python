# if else
# print("Welcome to the rollercoaster!")
# height = int(input("How tall are you in inches?\n"))
# >, <, >=, <=, !=, ==
# if height >= 36: 
#     print("GO ON IN HAVE FUN")
# else:
#     print("Sorry shawty, no ride for you.")

# Odd or Even exercise
# number = (int(input("Enter a number to check if it's odd or even:\n")))
# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

# elif - the dumbest syntax in existence
# nested if else
# print("Welcome to the rollercoaster!")
# height = int(input("How tall are you in inches?\n"))
# # >, <, >=, <=, !=, ==
# if height >= 36:
#     print("Welcome to the ticket line.")
#     age = int(input("How old are you?\n"))
#     if age >= 18: 
#         print("GO ON IN HAVE FUN")
#     else:
#         print("Sorry young gun, only old people.")
# else:
#     print("Sorry shawty, no ride for you.")

# Leap year exercise
# is a leap year if evenly divisible by 4
# except if it's evenly divisible by 100
# unless the year is also evenly divisible by 400

# year = int(input("Enter a year to check: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             is_leap_year = True
#         else:
#             is_leap_year = False
#     else:
#         is_leap_year = True
# else:
#     is_leap_year = False

# if is_leap_year == True:
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# print("Welcome to the rollercoaster!")
# height = int(input("How tall are you in inches?\n"))
# >, <, >=, <=, !=, ==
# if height >= 36:
#     print("Welcome to the ticket line.")

#     scared = input("Are you scared? Y or N.\n")
#     if scared == 'Y':
#         print('K have a good day. Bye.')
#     else:
#         age = int(input("How old are you?\n"))
#         if age >= 18: 
#             print("GO ON IN HAVE FUN")
#         else:
#             print("Sorry young gun, only old people.")
# else:
#     print("Sorry shawty, no ride for you.")

# Pizza order exercise
# print("Welcome to Python Pizza!")
# price = 0
# size = input("What size pizza do you want? S, M or L\n")
# if size == "S":
#     price += 15
#     add_pepperoni = input("Do you want pepperoni? Y or N.\n")
#     if add_pepperoni == "Y":
#         price += 2
#     add_cheese = input("Do you want extra cheese? Y or N.\n")
#     if add_cheese == "Y":
#         price += 1
# elif size == "M":
#     price += 20
#     add_pepperoni = input("Do you want pepperoni? Y or N.\n")
#     if add_pepperoni == "Y":
#         price += 3
#     add_cheese = input("Do you want extra cheese? Y or N.\n")
#     if add_cheese == "Y":
#         price += 1
# elif size == "L":
#     price += 25
#     add_pepperoni = input("Do you want pepperoni? Y or N.\n")
#     if add_pepperoni == "Y":
#         price += 3
#     add_cheese = input("Do you want extra cheese? Y or N.\n")
#     if add_cheese == "Y":
#         price += 1
# print(f"Your total is: ${price}.")

# and, or, not
# a = 12
# if a > 10 and a < 13:
#     print("BLOOP")
# not a > 15 -- flips from False to True

# print("clementine".count('e')) # 3

# Love calculator exercise
# print("Welcome to the love calculator!")
# name1 = input("What is your name? \n").lower()
# name2 = input("What is their name? \n").lower()
# true_count = 0
# love_count = 0
# true_count += name1.count('t')
# true_count += name1.count('r')
# true_count += name1.count('u')
# true_count += name1.count('e')
# true_count += name2.count('t')
# true_count += name2.count('r')
# true_count += name2.count('u')
# true_count += name2.count('e')
# love_count += name1.count('l')
# love_count += name1.count('o')
# love_count += name1.count('v')
# love_count += name1.count('e')
# love_count += name2.count('l')
# love_count += name2.count('o')
# love_count += name2.count('v')
# love_count += name2.count('e')
# percentage = str(true_count) + str(love_count)
# print(f"Your chances of true love are: {percentage}%")

# Day 3 Project - Choose your own adventure
# It's just a bunch of if statements I know how to make it but ain't nobody got time for that