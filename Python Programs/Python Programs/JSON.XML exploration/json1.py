import json

with open ('data.json') as f:
	data = json.load(f)
print(data)


with open('data1.json', 'w') as f:
	json.dump(data,f)
	str1 = json.dumps(data)
print(str1)
#with open('data1.json', 'r') as f:
	


stringdata = json.loads(str1)
print(stringdata)



