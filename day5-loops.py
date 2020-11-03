import random
# fruits = ['Apple', 'Peach', 'Pear']

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# Average height exercise - no using len() or sum()
student_heights = [180, 124, 165, 173, 189, 169, 146]
students = 0 # would normally use len()
total_height = 0
for height in student_heights:
    total_height += height
    students += 1
average_height = round(total_height / students)
print(f"The average student height is {average_height}")

# High Score exercise - no using max()
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(highest_score)

# range
for number in range(1, 10): # excludes 10 - can specify step range(1, 10, 2) steps by 2
    print(number)

# adding evens exercise - from 1 to 100
evens_total = 0
for evens in range(2,101,2):
    evens_total += evens
print(evens_total)

# Freaking fizzbuzz
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)

# Day 5 Project - Password Generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ''
for letter in range(1,nr_letters + 1):
    password += random.choice(letters)
for symbol in range(1,nr_symbols + 1):
    password += random.choice(symbols)
for number in range(1,nr_numbers + 1):
    password += random.choice(numbers)
print(f"{password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for letter in range(1,nr_letters + 1):
    password_list += random.choice(letters)
for symbol in range(1,nr_symbols + 1):
    password_list += random.choice(symbols)
for number in range(1,nr_numbers + 1):
    password_list += random.choice(numbers)
random.shuffle(password_list)
scrambled_password = ""
for char in password_list:
    scrambled_password += char
print(scrambled_password)