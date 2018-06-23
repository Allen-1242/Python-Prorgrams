#stack data type, stack works on first in last out , much like stacking things and removing vaklues from the top. We hvae used push,pop,print,peek, check if empty functions along with a basic menu display.
class test:
	def __init__(self):
		print("in the test")

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None	

class stack:
	def __init__(self):
		self.head = None

	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def pop(self):
		print("the removed data is :")		
		print(self.head.data)
		self.head = self.head.next
	
	def peek(self):
		print(self.head.data)
	
	def empty(self):
		if(self.head == None):
			print("The stack is empty")	
	
	def printl(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next

stack1 = stack()

print("Welcome to the stack dataset")

while(True):
	print("Menu \n 1.Push a value in the stack \t 2.Pop the top value \t 3.View the top 			element \n 4.Print the entire stack  5.Check if empty\t 6. Exit")
	imp = input("Enter the option that is needed : \n")	
	if(imp == 1):
		stkp = input("Enter the stack value \n")
		stack1.push(stkp)
		continue
	
	elif(imp == 2):
		print("Top value has been popped \n")
		stack1.pop()
		continue
	
	elif(imp == 3):
		print("The top of the stack is:")
		stack1.peek()
		continue	

	elif(imp == 4):
		print("The stack contents are: \n")
		stack1.printl()
		continue
	
	elif(imp == 5):
		stack1.empty()

	elif(imp == 6):
		break
