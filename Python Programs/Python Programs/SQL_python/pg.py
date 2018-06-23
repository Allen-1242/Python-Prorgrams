import psycopg2

conn =  psycopg2.connect(database = "test1", user = "postgres")
print("Open the database sucessfully")

cur = conn.cursor()

cur.execute(''' CREATE TABLE Student1(
		id INTEGER
		name TEXT
		salary FLOAT
		dept INTEGER
		);''')

print("table excuted")

cur.execute ('''INSERT INTO Student1 VALUES(1, 'Manoj T', 25000, 1);''')
cur.execute ('''INSERT INTO Student1 VALUES(2, 'Allen', 35000, 2);''')
cur.execute ('''INSERT INTO Student1 VALUES(3, 'BoB', 55000, 5);''')

print("the values are inserted")

r = cur.execute('''SELECT * FROM Student10''')
p = r.fetchall();
print(p)

conn.commit()
conn.close()




