print("Welcome to the data structures programs")
print("Enter the data structre you want to implemet")
while(True):
	print("Menu \n 1.Stacks \t 2.Queues \t 3.Singly Linked lists \n 4.Doubly Linked Lists  	5.Circular Lists\n 6.Doubly Linked Circular Lists 7.Binary Trees\t 			         8.Dictionaries\t 9.Exit")
	imp = input("Enter the option that is needed : \n")	
	if(imp == 1):
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
		
		


	if(imp == 2):
#queues work on te principle of first in first out , rather the queue is like a line of people

		class Node:
			def __init__(self,data):
				self.data = data
				self.next = None
	
		class queue:
			def __init__(self):
				self.head = None
				#self.last = None
			def enqueue(self,new_data):
				new_node = Node(new_data)
				new_node.next = self.head
				self.head = new_node
				self.last = None
				#print(self.last.data)
	
			def dequeue(self):
				temp = self.head    #temp moves from head to the last node, 
		 		temp1 = self.head	#temp1 moves from head to temp-1 node
				print("in the dequeue")	#temp1.next  = none, therby removing the link.	
				while(temp):
					temp = temp.next
					if(temp.next == None):
						print(temp.data)				
						break
		
				while(temp1):
					temp1 = temp1.next
					#print(temp1.data)
					if(temp1.next == temp):
						break
				temp1.next = None
		
	
			def printl(self):
				temp =self.head
				while(temp):
					print(temp.data)
					temp = temp.next
	
			def get_front(self):
					print(self.head.data)
	
			def is_empty(self):
					if(self.head == None):
						print("The queue is empty")


		q = queue()
		'''q.enqueue(3)
		q.enqueue(4)
		q.enqueue(5)
		q.dequeue()
		q.enqueue(6)
		q.printl()'''

		print("Welcome to the queue dataset")

		while(True):
			print("Menu \n 1.Push a value in the queue \t 2.Pop the top value \t 3.View the top 			element \n 4.Print the entire queue  5.Check if empty\t 6. Exit")
			imp = input("Enter the option that is needed : \n")	
			if(imp == 1):
				qtkp = input("Enter the queue value \n")
				q.enqueue(qtkp)
				continue
	
			elif(imp == 2):
				print("First value in the queue has been removed:\n")
				q.dequeue()
				continue
	
			elif(imp == 3):
				print("The front of the queue is:")
				q.get_front()
				continue	

			elif(imp == 4):
				print("The queue contents are: \n")
				q.printl()
				continue
	
			elif(imp == 5):
				q.is_empty()

			elif(imp == 6):
				break

	
