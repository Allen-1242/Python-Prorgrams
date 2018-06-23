#Miniproject 3
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None	

class stocks:
	def __init__(self):
		self.head = None
	
	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
		
class company:
	def __init__(self):
		self.head = None
		
		
	def add(self):
		self.comp = input("Enter the company needed \n")
		self.shares = int(input("Enter the total number of shares \n"))

	def remove(self,comp):
		
		
	def print1(self):
		print("company name:", self.comp)
		print("Shares:", self.shares)
		print("share value:", self.shares*3000)
		total_value = self.shares*3000	
		print(total_value)

st1 = stocks()	

print("Welcome to your stock portfolio, enter what company you wish to view")
while(True):
	print("Menu \n 1. Add a company  \t 2.Pop the top value \t 3.View the top 			element \n 4.Print the portfolio  5.Check if empty\t 6. Exit")
	imp = input("Enter the option that is needed :")	
	count = 0
	if(imp == 1):
		c1 = company()
		c1.add()
		st1.push(c1)
		continue
	
	if(imp == 2):
		c1.remove()	
		continue
	
	if(imp == 4):
		while(st1.head):
			print(st1.head.data.print1())	
			st1.head = st1.head.next			
					
		continue
