'''def y(msg):
	print(msg)

y("hello")

x = y
x("this is in x")

y = y
y('this is in y')


def indirect(func,msg):
	func(msg)
indirect(y,"this is sparta")

#def another(next,blah)
	
l = {(y,'spam'), (y,'seccind')}
for(func,q) in l:
	func(q)

y.count=0
y.a=20
print(dir(y))'''

'''def one(msg):
	def print1():
		print(msg)
		print(locals())

	return print1


pn = one("this is printed")
pn()'''

'''def func(a: 'this is printed', b: (1, 2), c: float) -> int:
	return a'''
'''l = [x*3 for x in range(-5,5) if x >0]
print(l)'''

'''from functools import reduce
r = reduce((lambda x,y: x*y),[1,2,3])
print(r)'''

'''l = [1,2,3,4]
it = iter[l]
#print(it)
next(it)'''

'''l = 'hello world'
l_iter = (x for x in l)     #next function is not being hit
print(l_iter)
print('In the loop')
next(l_iter)'''




'''import sys 
print(sys.platform)'''


l =['a', 'b', 'c', 'q', 1, 3, 4]
print(l)
(l.sort())
print(l)
l.insert(1, 'a')
print(l)

