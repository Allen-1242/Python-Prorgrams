#login stuff

import os
print("Hello! Welcome to the internet thing , please select if you have an accout or are new")
select = int(input("If new user enter 1,  else enter 2 \n"))
if select == 1:
	print("Welcome new User, please enter Username and Password as specified")
	user = input("Username:")
	password = input("Password:")
	os.mkdir(user)	
	os.chdir(user)	
	print(os.getcwd())
	print(user,password)
	cartno = input("enter the cart number that is needed in words")
	os.mkdir(cartno)
	os.chdir(cartno)
	print(os.getcwd())
	end = 1	
	while(end ==1):
		choice = input("the inventory list you can select are:")
		print("1.Bedsheet \n 2.covers \n 3.Exit")	
		if end == 1:
			if choice == 1:
				print("Bedsheet \n")
			elif choice == 2:
				print("Covers \n")
			elif choice == 3:
				end == 0							
				continue
		else:
			break
	
	
	
	

	
else:
	print("entered in the old")



