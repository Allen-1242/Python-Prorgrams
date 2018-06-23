class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class cll:
	def __init__(self):
		self.head = None
		self.prev = None

#pushing to the top of the list / inserting
	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
		
 

#removing from the top / poping 
	def pop(self): 		
		self.head = new_node.next
		new_node.next = None
#printing a list	
	def printcll(self):
		temp = self.head
		count = 0
		while(temp):
			print(temp.data)
			temp = temp.next
			if(temp == self.head):
				break

#inserting after a node
	def insert(self,new_data, index):
		self.index = index
		temp = self.head
		#temp1 = self.head
		new_node = Node(new_data)
		count = 1
		while(True):
			print(count+1)
			temp = temp.next
			count += 1
                        print(count)
			if(count == index):
				print(temp.data)				
				break
		
		new_node.next = temp.next
		temp.next = new_node
		print("in the loop")

#delteing a node
	def dell(self, index):
		self.index = index
		temp = self.head
		new_node = Node(new_data)
		count = 0
		while(temp):
			temp = temp.next
			count += count +1
			if(count == index):
				break
		temp.next  = None
		temp = temp.next

		
		
		

c1 = cll()
#c1.push(3)
#c1.push(4)
#c1.push(8)
#c1.push(5)
#c1.dell(3)
c1.insert(6,2)
c1.printcll()

'''class ListNode:  
	def __init__(self, data):
		self.data = data
        	self.next = None
       		 return

class SingleLinkedList:  
	def __init__(self):
		self.head = None
		self.tail = None
        	return
	    
	def add_list_item(self, item):
       		 if not isinstance(item, ListNode):
            		item = ListNode(item)

       		 if self.head is None:
            		self.head = item
       		 else:
            		self.tail.next = item

       		 self.tail = item

        	 return
	
	def list_length(self):

        	count = 0
        	current_node = self.head

        	while current_node is not None:
            		count = count + 1
            		current_node = current_node.next

       		return count

	

	def output_list(self):
		 current_node = self.head

        	 while current_node is not None:
           		 print(current_node.data)


            	 current_node = current_node.next

        	 return
'''








