from hashlib import *

userpass = {"bob": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"}

valid_input = False
while valid_input == False:
	user_input = input("Sign up or log in? signup/login ")
	if user_input == "login":
		valid_input = True
		valid_user = False
		while valid_user == False:
			username = input("Please enter your username. ")
			if username in userpass:
				valid_user = True
				valid_password = False
				while valid_password == False:
					passhash = sha256(input("Please enter your password. ").encode('utf-8')).hexdigest()
					print(passhash)
					if passhash == userpass[username]:
						valid_password = True
						print("Congratulations! You have logged in. ")
					else:
						print("Wrong password. Please enter a valid password. ")
				
			else:
				print("Wrong username. Please enter a valid username. ")
		
		
	elif user_input == "signup":
		valid_input = True
		user_taken = True
		while user_taken == True:
			username = input("Please enter the username that you want. ")
			if username in userpass:
				print("That username is taken. Please choose another one. ")
			else:
				user_taken = False
		passhash = sha256(input("Please enter the password that you want. ").encode('utf-8')).hexdigest()
		userpass[username] = passhash
		print("You have successfully signed up!")
	else:
		print("Please enter 'signup' or 'login'.")