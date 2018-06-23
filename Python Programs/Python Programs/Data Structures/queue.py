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

