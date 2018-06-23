#circular linked list 

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class clink:
	def __init__(self):
		self.head = None

	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		#self.head = new_node
		
		tempr =self.head
		while(tempr.next != self.head):
			tempr = tempr.next
		tempr.next = new_node
		
	
	def printlist(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next

links = clink()
links.push(3);
links.push(4)
links.push(5)
links.push(6)
links.printlist();
