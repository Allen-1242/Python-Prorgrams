'''#array before 6 and after 7 
print("Welcome, please enter the array\n")
num_array = list()
num_array1 = list()
	
num = input("Enter how many elements you want:")
print ("Enter numbers in array:")
for i in range(int(num)):
	  n = input("num :")
	  num_array.append(int(n))
print ('ARRAY: ',num_array)

print(num_array.index(6))
#print(num_array.index(7))

for i in range(int(num)):
	if i< num_array.index(6): 
		num_array1.append(num_array[i])
		#print((num_array1))
	if i> num_array.index(7): 
		num_array1.append(num_array[i])
		print((num_array1))
print((sum(num_array1)))'''


a = input("enter the value of a \n")
if(a == 5): #or (a==4):	
	print("this is in a")
else:
	print("this is not in a")
		









