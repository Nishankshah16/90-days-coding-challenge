from random import shuffle, randint, choice

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password():

	password_letter=[choice(letters) for _ in range(randint(8,10))]
	password_number=[choice(numbers) for _ in range(randint(2,4))]
	password_symbol=[choice(symbols) for _ in range(randint(2,4))]
	# for i in range(0,nr_letters+1):
	# 	password.append(random.choice(letters))
	# for i in range(0,nr_symbols+1):
	# 	password.append(random.choice(symbols))
	# for i in range(0, nr_numbers+1):
	# 	password.append(random.choice(numbers))
	password = password_letter + password_number + password_symbol
	shuffle(password)
	a=''.join(password)
	return a
