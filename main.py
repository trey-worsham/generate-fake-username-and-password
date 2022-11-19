import random
import secrets

def generate_username(sex):
	if sex == 0:
		List_of_first_names = open('man_name').read().splitlines()
	else:
		List_of_first_names = open('woman_name').read().splitlines()

	first_name = random.choice(List_of_first_names)

	List_of_last_names = open('last_name').read().splitlines()
	last_name = random.choice(List_of_last_names)

	return(first_name+"_"+last_name+"_"+str(random.randint(0, 1000)))

def generate_password():
	bits = secrets.randbits(200)
	bits_hex = hex(bits)
	private_key = bits_hex[2:]
	return(private_key)

def generate_username_and_password():
	print("would you like a woman's name or a man's name")
	print("0 for man's name")
	print("1 for woman's name")
	print("6 for exit")
	x = input("input : ")

	if x == "1" or x == "0":
		print(generate_username(x))
		print(generate_password())
	else:
		if x == "6":
			pass
		else:
			generate_username_and_password()
