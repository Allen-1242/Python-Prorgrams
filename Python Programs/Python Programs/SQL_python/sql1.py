import sqlite3

con = sqlite3.connect('my_data.db')

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Student10(id NUMBER, name VARCHAR(20));''')
print("in the table")
for i in range(1):
	f = int(input("enter the value\n"))
	k = input("enter the name")

cur.execute('''INSERT INTO Student10 VALUES(?,?);''',[f,k])
print("has been inserted")
r = cur.execute('''SELECT * FROM Student10''')
r = r.fetchall();
print(r)

cur.execute('''UPDATE Student10 SET id=6 WHERE name='CACTUS' ''')
print("in the execute")
con.commit()

con.close()
