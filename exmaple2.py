from collections import Counter

number_array = list()
num = input("Enter the age of the neice:")
print ('Enter cnadle heights: ')
for i in range(int(num)):
    n = input("number :")
    number_array.append(int(n))
print ('Candle Height: ',number_array)

#finding largest value in the list 
b = max(number_array)
print(b)

#Counting the number of largest values in the list 
d = number_array.count(b)
print(d)

#Total number of breaths
a = len(set(number_array))
print( "The final number of breaths that the neice needs to take is")
print(a)

s
