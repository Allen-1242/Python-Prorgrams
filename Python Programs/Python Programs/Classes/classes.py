'''class Taxi:
	def __init__(self,drivername,driverid):
		self.dname = drivername
		self.driverid = driverid
		numpassengers = 0
	def printdriver(self):
		print(self.dname)
	
	def printdriverid(self):
		print(self.driverid)	
	def pickup(self,numpassengers)
		self.numpassengers+= numpassengers

t1 = Taxi('a','1')
t2 = Taxi('b')
t3 = Taxi('c')

t1.printdriver()
t1.printdriverid()
t2.printdriver()
t3.printdriver()'''


'''class bus:
	def __init__(self,color,name,seatno):
		self.color1 = color
		self.name1 = name
		self.seatno = seatno
	
	def color(self):
		print(self.color1)
	def name(self):
		print(self.name1)
	def outbus(self, seatno):
		self.seatno-=seatno
		print(self.seatno)
	def inbus(self,seatno):
		self.seatno+=seatno
		print(self.seatno)
		

b1 = bus('red','bob',3)
b2 = bus('blue', 'dum', 10)
b1.color()
b1.name()
b1.outbus(2)
b1.inbus(4)
b2.color()
b2.inbus(4)'''

'''class bus:
	numbus = 0
	@classmethod
	def how_many(cls):
		print("in the class")		
		print(cls.numbus)
		return cls.numbus
		
	def __init__(self,color,name,seatno):
		self.color1 = color
		self.name1 = name
		self.seatno = seatno
	
	def color(self):
		print(self.color1)
	def name(self):
		print(self.name1)
	def outbus(self, seatno):
		self.seatno-=seatno
		print(self.seatno)
	def inbus(self,seatno):
		self.seatno+=seatno
		print(self.seatno)
		

b1 = bus('red','bob',3)
b2 = bus('blue', 'dum', 10)
b1.color()
b1.name()
b1.outbus(2)
b1.inbus(4)
b2.color()
b2.inbus(4)
b1.numbus = b1.numbus+1'''


'''class rec:
	pass


rec.name = 'bob'
print(rec.name)
x = rec()
y = rec()
x.name = 'sue'
print(x.name,y.name,rec.name)'''

'''class person:
	def __init__(self,name,jobs,age):
		self.name = name
		self. jobs= jobs
		self.age = age	
	def infoz(self):
		print(self.name, self.jobs)

rec1 = person('bob', ('gardner', 'death'), 32)

rec1.infoz()'''
'''if __name__ == '__main__':
	n = int(input())
	for i in range(n+1):
		if i == 0:
			continue        	
		print(i, end='')'''
i = 0 
while i <10:
     i += 1 
     print (i,end="")

	
