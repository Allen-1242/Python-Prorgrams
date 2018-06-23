#doubly linked list, has two pointers pointing front and back thus we can go foreword and backwards in a list.Usual list only supports foreword operations
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

class sll:
	def __init__(self):
		self.head = None

	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
		self.prev = None
	
	def insert(self,new_data,index):
`		new_node = Node(new_data)
		temp = self.head
		temp1 = self.head
		count = 1
		while(temp!=None) and (count!=index):
			count = count +1
			temp = temp.next
		
		temp1 = temp.next
		temp.next = new_node.prev
		new_node.next = temp1.prev
		temp1.prev = new_node
		new_node.prev = temp
	
	def print1(self):
		

		
