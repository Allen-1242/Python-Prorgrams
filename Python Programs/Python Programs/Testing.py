l1 = input()
l2 = input()
count = 0
count1 = 0
for i in range(len(l1)):
	for j in range(len(l2)):
		if l1[i]>l2[j]: 
			print(l1[1])			
			count1+=1
		elif l1[i]<l2[j]: 
			count+=1
		elif l1[i]==l2[j]:
			base=0
print(count1,count)
		

rec = {'name':{'first':'bob', 'last':'kelso'}, 
	'title':['dev', 'sand', 'dum'], 
	'age': 34}
'''if 'f' not in rec:
	print("Missing stuff")'''
k = (list(rec.keys()))
k.sort()
print(k)
print(rec)
print(rec['name']['first'])
print(rec['title'][1])

rec = {'name':{'first':'bob', 'last':'kelso'}, 
	'title':['dev', 'sand', 'dum'], 
	'age': 34}
'''if 'f' not in rec:
	print("Missing stuff")'''
k = (list(rec.keys()))
k.sort()
print(k)
print(rec)
print(rec['name']['first'])
print(rec['title'][1])

