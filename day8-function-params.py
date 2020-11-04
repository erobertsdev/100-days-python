import math

def greet(name):
    print(f"hey {name}")
    print(f"hi {name}")
    print(f"hello {name}")

greet('Eli')

def greet_with(name, location):
    print(f"Greetings {name} from {location}!")

greet_with('Elias','Jupiter')
greet_with(name='Jupiter', location='Elias')

# paint can exercise
def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")

paint_calc(22,5,3)

# prime number checker exercise
def prime_checker(num):
    is_prime = True
    for divisor in range(2,num):
        if num % divisor == 0:
            is_prime = False
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is NOT a prime number.")
        
n = int(input("Number to check: "))
prime_checker(n)

# caesar cipher exercise

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         if new_position > len(alphabet):
#             new_position = -1 + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         if new_position < 0:
#             new_position = len(alphabet) - 1 - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The decoded text is {plain_text}")

# if direction == 'encode':
#     encrypt(text, shift)
# elif direction == 'decode':
#     decrypt(text, shift)
# else:
#     print('Invalid input')

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if cipher_direction == "decode":
                shift_amount *= -1
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is: {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 25
    caesar(text, shift, direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False
        print('Goodbye.')


