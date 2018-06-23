'''class Node:
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
	
	def printList(self):
		temp = self.head
		if self.head is not None:
			while(temp):
				print(temp.data)
				temp = temp.next
			      	if (temp == self.head):
				   	break

sl = sll()
sl.push(3)
sl.push(4)
sl.push(5)
sl.printList'''





#array before 6 and after 7 



print("welcome, please enter the array\n")
num_array = list()
num_array1 = list()
v = 6
l = 7
num = input("Enter how many elements you want:")
print ("Enter numbers in array:")
for i in range(int(num)):
    n = input("num :")
    num_array.append(int(n))
print ('ARRAY: ',num_array)

print(num_array.index(6))



for i in range(int(num)):
	if (i< num_array.index(6) 
		num_array1.append(num_array[i])
		print((num_array1))
	
print((num_array1))
		

















