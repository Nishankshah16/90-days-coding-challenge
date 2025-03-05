#Method 1

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=[]
for i in range(0,nr_letters+1):
    password.append(random.choice(letters))
for i in range(0,nr_symbols+1):
    password.append(random.choice(symbols))
for i in range(0, nr_numbers+1):
    password.append(random.choice(numbers))

random.shuffle(password)
a=''.join(password)
print(a)


#method 2 anuja
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']

print("Welcome to the PyPassword generator")
nr_letter = int(input("How many letters would you like like in your password? "))
nr_symbol = int(input("How many symbol would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

pwd = []

for char in range(1, nr_letter + 1):
	random_char = random.choice(letters)
	pwd += random_char

for num in range(1, nr_symbol + 1):
	random_sym = random.choice(symbols)
	pwd += random_sym

for sym in range(1, nr_numbers + 1):
	random_num = random.choice(numbers)
	pwd += random_num

random.shuffle(pwd)

password = ""
for i in pwd:
	password += i

print(f'Your password is : {password}')

#use in day 29
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password():
	nr_letters= random.randint(8,10)
	nr_symbols = random.randint(2,4)
	nr_numbers = random.randint(2,4)

	password=[]
	for i in range(0,nr_letters+1):
		password.append(random.choice(letters))
	for i in range(0,nr_symbols+1):
		password.append(random.choice(symbols))
	for i in range(0, nr_numbers+1):
		password.append(random.choice(numbers))

	random.shuffle(password)
	a=''.join(password)
	return a
