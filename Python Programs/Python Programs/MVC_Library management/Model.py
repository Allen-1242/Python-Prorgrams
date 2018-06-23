import sqlite3
from datetime import datetime
con = sqlite3.connect('ph1.db')

cur = con.cursor()

class user:
	
	def user_cr():
		cur.execute('''CREATE TABLE IF NOT EXISTS Users(id NUMBER, name VARCHAR(20), Address VARCHAR(20), PhoneNum NUMBER);''')
	
	def user_ins():
		for i in range(1):
			a = int(input("Enter the ID Number\n"))
			b = input("Enter the name \n")
			c = input("Enter the current Address \n")
			d = int(input("Enter the current phone Number"))

		cur.execute('''INSERT INTO Users VALUES(?,?,?,?);''',[a,b,c,d])
		con.commit()

	def user_read():
		r = cur.execute('''SELECT * FROM Users''')
		r = r.fetchall();
		print(r)

	def user_name():
		r = cur.execute('''SELECT name FROM Users''')
		r = r.fetchall();
		res_list = [x[0] for x in r]
		a = "".join( repr(e) for e in res_list )
		return ("".join( repr(e) for e in res_list ))		

	def user_table():
		cur.execute('''CREAT1E TABLE IF NOT EXISTS %s(Author VARCHAR(20), Books_name VARCHAR(20), Fee Number);'''%(a))


class Books:

	def books_read():
		r = cur.execute('''SELECT * FROM Books''')
		r = r.fetchall();
		return r



u1 = user
b1 = Books




