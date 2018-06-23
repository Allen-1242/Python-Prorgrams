# clinklists
 
class Node:
     
    def __init__(self, data):
        self.data = data 
        self.next = None
 
class CLinkedList:
     
    def __init__(self):
        self.head = None
 
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head
         
        ptr1.next = self.head
 
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = ptr1
 
        else:
            ptr1.next = ptr1 
 
        self.head = ptr1 
 
    def printList(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print(temp.data)
                temp = temp.next
                if (temp == self.head):
                    break




cllist = CLinkedList()
 
cllist.push(1)
cllist.push(2)
cllist.push(3)
cllist.push(4)
 
print "Contents of circular Linked List"
cllist.printList()

#stacks , first in last out 

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

	#def pop(self):
		
	
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
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.peek()
print("the values of the stacks are:")
stack1.printl()
stack1.empty()'''


'''#Queues first in first out 

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
	
class queue:
	def __init__(self):
		self.head = None
	
	def enqueue(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
	
	def dequeue(self):
		temp = self.head
		print("in the dequeue")		
		last = self.head
		last.next =None			
		while(temp.next!=last.next):
			#if(temp.next == None):
				#print(temp.data)
				#break
			temp = temp.next
		temp.next =None
	
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
q.enqueue(3)
q.enqueue(4)
q.enqueue(20)
q.get_front()
q.printl()
q.dequeue()
q.printl()
q.get_front()	


		
