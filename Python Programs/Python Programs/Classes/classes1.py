#operator overlaoding
'''class A:
	def __init__(self,data):
		self.data = data
	
	def __add__(self,newval):
		#self.newval = newval
		return (self.data - newval.data)

a = A(20)
b = A(20)
print(a+b)'''

#context Mapper

'''with open ('day4.py', 'r') as f1:
	print(f1.read())'''

#with allows us to open files wihtout needing to close them

'''class A:
	def __init__(self,data):
		self.data = data
	
	def __enter__(self)'''

'''with open ('day4.py', 'a') as f1:
	with open ('day3.py', 'r') as f2:	
		f1.write(f2.read())'''


#inheritence

'''class P:
	def __init__(self,datap):
		self.datap = datap
class I:
	def __init__(self, datai,datap):
		super().__init__(datap)
		self.datai = datai 
		

a = I('10','20')
print (a.datai, a.datap)'''

#polymorphism

#operator ovrelaoding, context manager ending, human and hipppo classes by tomorow 



		

		

