def whitespace(str):	
	str = str.replace(" ","")
	print(str)

#whitespace("this is test")

'''def strcount(str1):
	for i in range(len(str1)):
		for j in range(len(str)):
			if str1[i] == str1[j]:
				count+=1
				print(count-1)
			while j == (len(str1):
				l1 = [str1[i]]
				l2 = [count]
				q = dict(zip(l1,l2))
				print(q)
		continue
	print(str)'''

#strcount('name is bob')

'''def filecount(str1)
	fp = open(str1,'+r')'''
	
def upper(str1):
	str1 = str1.upper()
	print(str1)

#upper('thsi is a test')

def lower(str1):
	str1 = str1.lower()
	print(str1)

#lower('THIS IS MY NAME')

def alphabet(str1):
	str1 = sorted(str1)
	print(str1)
#alphabet('awsrfes')

def find(str1,str2,str3):
	if str1 in str2:
		q = str2.find(str1)
		str2 = str2.split(str1)
		print(str2)
		str2.insert(q ,str3)
		print(str2)
	else:
		print("not needed")
#find('bce', 'abced', 'qwerty')'''

def palindome(str1):
	str_rev = reversed(str1)
	print(list(str_rev))
	print(list(str1))	
	if (list(str1) == list(str_rev)):
		print("this is a palindrime")
	else:
		print("this is not a palindrome")
	
#palindome("daad")
		


