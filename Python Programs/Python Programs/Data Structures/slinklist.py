#singly linked lists work mainly like that of a stack, excpt we can delete thigns from anywhere and add nodes anywhere. Both stacks and queues work like lists, with some retstrctions.
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class sll:
	def __init__(self):
		self.head = None

	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
	
	def insert(self,new_data,index): #inserts a node after a certain index
		new_node = Node(new_data)
		count = 1
		temp = self.head
		while((temp.next!=None) and (count != index)):
			count = count +1
			temp = temp.next
		new_node.next = temp.next
		temp.next = new_node

	def delete(self,index):#delete a node after an index
		count = 1
		temp = self.head
		temp1 = self.head
		while((temp.next!=None) and (count != index)):
			count = count + 1
			temp = temp.next #temp1 goes to the node to be delted
		temp1 = temp.next        # temp.next = temp1.next, removing the node on temp1
		temp.next = temp1.next   #temp = temp1.next, moving the poitner to the new node
		temp1 = temp1.next
		
	def printList(self):
        	temp = self.head
       		if self.head is not None:
           		while(temp):
              	  		print(temp.data)
                		temp = temp.next
              			if (temp == self.head):
                   			break

sl = sll()
'''sl.push(3)
sl.push(5)
sl.push(8)
sl.push(9)
sl.insert(4,3)
sl.delete(3)
sl.printList()'''

print("Welcome to the singly linked list dataset")

while(True):
	print("Menu \n 1.Push a value in the list \t 2.Insert a new node anywhere \t 3.Delete a node anywhere \n 4.Print the entire list 5. Exit")
	imp = input("Enter the option that is needed : \n")	
	if(imp == 1):
		stkp = input("Enter the list value \n")
		sl.push(stkp)
		continue
	
	elif(imp == 2):
		print("First enter the node and then the index:\n")
		sl.insert(ind,nd)
		continue
	
	elif(imp == 3):
		print("Enter the index to be deleted:")
		ind = int(input())
		sl.delete(ind)
		continue	

	elif(imp == 4):
		print("The list contents are: \n")
		sl.printList()
		continue
	
	elif(imp == 5):
		break

	
		
