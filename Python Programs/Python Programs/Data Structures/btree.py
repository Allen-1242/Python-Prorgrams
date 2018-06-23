#binary tree , two nodes, left and right , left is lesser than the node or the right node, and so on

class Node:
	def __init__(self,data):
		self.data = data
		self.rptr = None
		self.lptr = None

class btree:
	def __init__(self):
		self.key = None
		self.trace = None

	def insert_root(self,new_data):#so i call the iset root node first and input data
		root_node = Node(new_data)
		self.key = root_node	
		print("root node sucessfully added")	
				
	def insertn(self,new_data):
		new_node = Node(new_data)
		if(new_node.data < self.key.data):
			self.key.lptr = new_node
		elif(new_node.data > self.key.data):
			self.key.rptr = new_node
		elif(new_node.data == self.key.data):
			self.key.rptr = new_node
		self.trace = new_node
		#print(self.trace.data)
	
	def tprint(self):
		print(self.key.data)
		if(self.key.rptr == True):
			self.key.rprt = self.key
			print(self.key.data)

		 	
		#print(self.trace.data)




def search(self,key,node = None):

		if node.key == key :
			print "key exists"
			return node

		elif key < node.key and node.left is not None:
			print "left"
			return self.search(key,node = node.left)
			
		elif key > node.key and node.right is not None:
			print "right"
			return self.search(key,node = node.right)
			
		else:
			print "key does not exist"
			return None
bt = btree()
bt.insert_root(3)
bt.insertn(5)
bt.insertn(2)
bt.tprint()



'''class Node:
   def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

def inOrder(root):
   if root:
       inOrder(root.left)
       print (root.data)
       inOrder(root.right)

def preOrder(root):
   if root:
       print (root.data)
       preOrder(root.left)
       preOrder(root.right)

def postOrder(root):
   if root:
       postOrder(root.left)
       postOrder(root.right)
       print (root.data)

#making the tree 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print inOrder(root)
#4 2 5 1 3
print preOrder(root)
#1 2 4 5 3
print postOrder(root)
#4 5 2 3 1'''
