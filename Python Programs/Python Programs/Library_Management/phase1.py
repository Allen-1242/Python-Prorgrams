import sqlite3
from datetime import datetime
con = sqlite3.connect('ph1.db')

cur = con.cursor()

print("Welcome to the StoneHill library")
while(True):
	ch = int(input("Enter the option\n1.User\n2.Administator\n3.Exit\n"))
	if(ch == 1):
		while(True):
			ch = int(input("Enter the option\n1.New User(Registration)\n2.Login\n3.Exit\n"))
			cur.execute('''CREATE TABLE IF NOT EXISTS Users(id NUMBER, name VARCHAR(20), Address VARCHAR(20), PhoneNum NUMBER);''')

			if(ch == 1):
				print("Welcome User, please enter the login details")
				#print("In the users function \n")
				#print("in the table")
			
				for i in range(1):
					a = int(input("Enter the ID Number\n"))
					b = input("Enter the name \n")
					c = input("Enter the current Address \n")
					d = int(input("Enter the current phone Number"))

				cur.execute('''INSERT INTO Users VALUES(?,?,?,?);''',[a,b,c,d])
				con.commit()	
			
				print("Has been inserted")
				r = cur.execute('''SELECT * FROM Users''')
				r = r.fetchall();
				print(r)
				
				print("Welcome to your dashboard",b)
				cur.execute('''CREATE TABLE IF NOT EXISTS %s(Author VARCHAR(20), Books_name VARCHAR(20), Fee Number);'''%(b))
				
				while(True):
					ch = int(input("1.Rent Books\n2.Return books\n3.Browse Libray\n4.Exit\n"))
					if(ch == 1):
						print("Welcome to the library, select the books wanted")
						r = cur.execute('''SELECT * FROM Books''')
						r = r.fetchall();
						print(r)
						print("The rent is 30 for 20 days")
						
						while(True):
							r =30 							
							z = input("Enter the Author name\n")
							y = input("Enter the book name\n")
							dt = datetime.now()
							strg = '{:%B %d %Y}'.format(dt)
							print(strg)	 						
							s = 'bob'							
							cur.execute('''INSERT INTO %s VALUES(%s,%s,%d);''' %(b,z,y,r))
							con.commit()
							
							print("Check in date is", strg)
							
							#cur.execute('''DELETE FROM Books WHERE Author_name = %s;'''%(z))
							ch = int(input("Do you wish to continue?\n1.Add More\n 2.Exit\n"))
							if(ch == 1):
								continue
							elif(ch == 2):
								break
							
					if(ch == 2):
						print("Welcome to book returning\n")
						
						print("Enter the book details\n")
						z = input("Enter the Author name")
						y = input("Enter the book name")
						t = int(input("Enter the date returned"))
	
						cur.execute('''DELETE FROM %s WHERE Author_name = %s;''' %(b,z))
						con.commit()

						ch = int(input("Do you wish to continue?\n1.Delete More\n2.Exit\n"))
						if(ch == 1):
							continue
						elif(ch == 2):
							break

					if(ch == 3):
						print("Welcome to the library, view the books availible")
						r = cur.execute('''SELECT * FROM Books''')
						r = r.fetchall();
						print(r)			 											
				
					if(ch == 4):
						break
				con.commit()
				
			
			if(ch == 2):
				
				print("Welcome, we value you patronage\n")
				passw = int(input("Enter the user id\n"))
				usern = input("Enter the user name\n")
				
				user_list_id = cur.execute('''SELECT id FROM Users''')
				user_list_id = user_list_id.fetchall()
				user_list_id = ([i for (i,) in user_list_id])
				
				user_list_name = cur.execute('''SELECT name FROM Users''')
				user_list_name = user_list_name.fetchall()
				user_list_name = ([i for (i,) in user_list_name])
				
				
				if passw not in user_list_id:
					print("invalid id\n")
					break
				else: 
					print("Welcome user",usern)
					
					print("Welcome to your dashboard",usern)
				cur.execute('''CREATE TABLE IF NOT EXISTS %s(Books_Rented NUMBER, Books_name VARCHAR(20), Rent Number);'''%(usern))
				
				while(True):
					ch = int(input("1.Rent Books\n2.Return books\n3.Browse Libray\n4.View Dash\n5.Exit"))
					if(ch == 1):
						print("Welcome to the library, select the books wanted")
						r = cur.execute('''SELECT * FROM Books''')
						r = r.fetchall();
						print(r)
				
						while(True):
							z = input("Enter the Author name")
							y = input("Enter the book name")
							r = 30
							cur.executescript('''INSERT INTO %s VALUES(%s,%s,%d);''' %(usern,z,y,r))
							
							#cur.executescript('''DELETE FROM Books WHERE Author_name LIKE "%(?)%";''', [z])
							con.commit()
							
							ch = int(input("Do you wish to continue?1.Add More\n 2.Exit\n"))
							if(ch == 1):
								continue
							elif(ch == 2):
								break
							
					if(ch == 2):
						print("Returning a book from a User\n")
						for i in range(1):
							a = input("Enter the authors name\n")
							b = input("Enter the book name \n")
							c = input("Enter the Publication Company\n")
			
							cur.execute('''DELETE FROM %s WHERE Author_name = %s;'''%(usern,a))
				
							ch = int(input("Do you wish to continue? 1.Delete More\n 2.Exit"))
							if(ch == 1):
								continue
							elif(ch == 2):
								break 

					if(ch == 3):
						print("Welcome to the library, view the books availible")
						r = cur.execute('''SELECT * FROM Books''')
						r = r.fetchall();
						print(r)

					if(ch == 4):
						print("Welcome to the dash\n")
						print("The books taken are:\n")
						r = cur.execute('''SELECT * FROM %s'''%(usern))
						r = r.fetchall();
						print(r)
					
					if(ch == 4):
						break
		 											
				con.commit()
				
					
				

			if(ch == 3):
				break
			break
		
		break
	
	elif(ch == 2):
		ch = int(input("Enter the option:\n1.New Librarian(Registration)\n2.Login\n3.Exit\n"))				
		cur.execute('''CREATE TABLE IF NOT EXISTS Librarians( id NUMBER, name VARCHAR(20), PRIMARY KEY(id), UNIQUE(name));''')

		#print("in the table")
		if(ch == 1):
			print("Entering new librarian Details\n")
			for i in range(1):
				f = int(input("Enter the ID\n"))
				k = input("Enter the Name\n")

				cur.execute('''INSERT INTO Librarians VALUES(?,?);''',[f,k])
				print("Has been inserted")
				break
			
							
			con.commit()
			
			r = cur.execute('''SELECT * FROM Librarians''')
			r = r.fetchall();
			print(r)

		
			ch = int(input("Enter the option:\n1.Add book\n2.Remove Book\n3.Edit Book\n4.View Library\n5.Exit\n"))
			if(ch == 1):
				while(True):	
					print("Adding a book to the libray")
					cur.execute('''CREATE TABLE IF NOT EXISTS Books(Author_name VARCHAR(20), Book_name VARCHAR(20), Publication Company VARCHAR(20));''') 				
					for i in range(1):
						a = input("Enter the authors name\n")
						b = input("Enter the book name \n")
						c = input("Enter the Publication Company\n")

					cur.execute('''INSERT INTO Books VALUES(?,?,?);''',[a,b,c])
					print("The current books are")
					
					r = cur.execute('''SELECT * FROM Books''')
					r = r.fetchall();
					print(r)
				
					ch = int(input("Do you wish to continue? 1.Add More\n2.Exit\n"))
					
					if(ch == 1):
						continue
					elif(ch == 2):
						break
		
			elif(ch == 3):
				print("Editing the book \n")
				for i in range(1):
					ch = int(input("Enter the options:\n1.Change Author\n2.Change the book name\n3.Change the Publishing Company\n4.Exit"))
					
					r = cur.execute('''SELECT * FROM Books''')
					r = r.fetchall();
					print(r)			
					
					if( ch == 1):
						print("Changing the Author\n")
						q = input("Enter the original name\n")
						a = input("Enter the authors name to be changed\n")
						cur.execute('''UPDATE Books SET Author_name=? WHERE Author_name=?''',[a,q]) 		
						
						r = cur.execute('''SELECT * FROM Books''')
						r = r.fetchall();
						print(r)
					
						print(a)
																					     
						con.commit() 									
					if( ch == 2):
						print("Changing the book\n") 							
						q = input("Enter the original book name\n") 							
						a = input("Enter the authors name to be changed\n")
						cur.execute('''UPDATE Books SET Book_name=? WHERE Book_name=?''',[a,q])									
						
						con.commit()
						r = cur.execute('''SELECT * FROM Books''')
						r = r.fetchall();
						print(r)
					
					if( ch == 3):
						print("Changing the Publication name\n")
						q = input("Enter the original publisher name\n") 							
						a = input("Enter the publisher name to be changed\n")
						cur.execute('''UPDATE Books SET Publication Company=? WHERE Publication Company=?''',[a,q])
						
						con.commit()
						r = cur.execute('''SELECT * FROM Books''')
						r = r.fetchall();
						print(r)


			elif(ch == 2):
				print("Removing a book from a library\n")
				for i in range(1):
					a = input("Enter the authors name\n")
					b = input("Enter the book name \n")
			
					r = cur.execute('''SELECT * FROM Books''')
					r = r.fetchall();
					print(r)
			
					cur.execute('''DELETE FROM Books WHERE Author_name = (?);''',[a])
					con.commit()
					
					ch = int(input("Do you wish to continue? 1.Delete More\n 2.Exit\n"))
					if(ch == 1):
						continue
					elif(ch == 2):
						break
		

			elif(ch == 4):
				print("Viewing the library\n")
				r = cur.execute('''SELECT * FROM Books''')
				r = r.fetchall();
				print(r)
		

			elif(ch == 5):
				break

		if(ch == 2):
			print("Welcome to Library Login Librarian\n")
			passw = int(input("Enter the Librarian id\n"))
			usern = input("Enter the Librarian name\n")
				
			lib_list_id = cur.execute('''SELECT id FROM Librarians''')
			lib_list_id = lib_list_id.fetchall()
			lib_list_id = ([i for (i,) in lib_list_id])
			
			lib_list_name = cur.execute('''SELECT name FROM Librarians''')
			lib_list_name = lib_list_name.fetchall()
			lib_list_name = ([i for (i,) in lib_list_name])
				
				
			if passw not in lib_list_id:					
				print("invalid id\n")
				break
			else: 
				print("Welcome Librarian",usern)


			ch = int(input("Enter the option:\n1.Add book\n2.Remove Book\n3.Edit Book\n4.View Library\n5.Exit"))
			if(ch == 1):
				while(True):	
					print("Adding a book to the libray")
					cur.execute('''CREATE TABLE IF NOT EXISTS Books(Author_name VARCHAR(20), Book_name VARCHAR(20), Publication Company VARCHAR(20));''') 				
					for i in range(1):
						a = input("Enter the authors name\n")
						b = input("Enter the book name \n")
						c = input("Enter the Publication Company\n")

					cur.execute('''INSERT INTO Books VALUES(?,?,?);''',[a,b,c])
					print("The current books are")
					r = cur.execute('''SELECT * FROM Books''')
					r = r.fetchall();
					print(r)
				
					ch = int(input("Do you wish to continue? 1.Add More\n2.Exit\n"))
					if(ch == 1):
						continue
					elif(ch == 2):
						break
		
			elif(ch == 3):
				print("Editing the book \n")
				for i in range(1):
					ch = int(input("Enter the options:\n1.Change Author\n2.Change the book name\n3.Change the Publishing Company\n4.Exit"))
					
					r = cur.execute('''SELECT * FROM Books''')
					r = r.fetchall();
					print(r)			
					
					if( ch == 1):
						print("Changing the Author\n")
						q = input("Enter the original name\n")
						a = input("Enter the authors name to be changed\n")
						cur.execute('''UPDATE Books SET Author_name=? WHERE Author_name=?''',[a,q]) 		
						
						r = cur.execute('''SELECT * FROM Books''')
						r = r.fetchall();
						print(r)
					
						print(a)
																					     
						con.commit() 									
					if( ch == 2):
						print("Changing the book\n") 							
						q = input("Enter the original book name\n") 							
						a = input("Enter the authors name to be changed\n")
						cur.execute('''UPDATE Books SET Book_name=? WHERE Book_name=?''',[a,q])									
						
						con.commit()
						r = cur.execute('''SELECT * FROM Books''')
						r = r.fetchall();
						print(r)
					
					if( ch == 3):
						print("Changing the Publication name\n")
						q = input("Enter the original publisher name\n") 							
						a = input("Enter the publisher name to be changed\n")
						cur.execute('''UPDATE Books SET Publication Company=? WHERE Publication Company=?''',[a,q])
						
						con.commit()
						r = cur.execute('''SELECT * FROM Books''')
						r = r.fetchall();
						print(r)


			elif(ch == 2):
				print("Removing a book from a library\n")
				#print("in the login page")
				for i in range(1):
					a = input("Enter the authors name\n")
					b = input("Enter the book name \n")
					
					r = cur.execute('''SELECT * FROM Books''')
					r = r.fetchall();
					print(r)
					
					cur.execute('''DELETE FROM Books WHERE Author_name = (?);''',[a])
					con.commit()
				
					ch = int(input("Do you wish to continue? 1.Delete More\n2.Exit\n"))
					if(ch == 1):
						continue
					elif(ch == 2):
						break
		

			elif(ch == 4):
				print("Viewing the library\n")
				r = cur.execute('''SELECT * FROM Books''')
				r = r.fetchall();
				print(r)
		

			elif(ch == 5):
				break

	elif(ch == 3):
		break

	else:
		print("Please enter a correct option \n")
		break

con.close()


