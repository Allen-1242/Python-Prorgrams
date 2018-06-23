import sqlite3

con = sqlite3.connect('my_data.db')

cur = con.cursor()

while(True):
	print("Welcome to the database")
	print("1.Insert the row\t2.View the table\n3.Update the table\t 4.Drop the table\n5.Exit")
	imp = int(input("Enter the operation needed"))	
	
	if imp == 1:
		print("Welcome to insertion \n")
		f = int(input("enter the id\n"))
		k = input("enter the name")
		cur.execute('''INSERT INTO Student10 VALUES(?,?);''',[f,k])
		
	if imp == 2:
		print("Welcome to viewing the table\n")
		r = cur.execute('''SELECT * FROM Student10''')
		p = r.fetchall();
		print(p)

	if imp == 3:
		print("Welcome to updating the table\n")
		k = input("enter the name to be changed")
		f = int(input("enter the id to be changed\n"))
		cur.execute('''UPDATE Student10 SET id=? WHERE name=? ''',[f,k])
		
	if imp == 4:
		print("Welcome to deleting the table\n")
		cur.execute('''DROP TABLE Student10''')	
	
	if imp == 5:
		print("Exited the program")
		break

