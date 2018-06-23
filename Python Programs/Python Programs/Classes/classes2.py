#hippoclass

class hippo:
	hippos = 0
	@classmethod
	def how_many(cls):
		print("in the class")		
		print(cls.hippos)
		return cls.hippos	
	
	def __init__(self,name,weight):
		self.name = name
		self.weight = weight
		hippo.hippos =hippo.hippos+ 1
	
	def feed(self,weight):
		self.weight = weight + 10
		print(self.weight)

	def workout(self,weight):
		self.weight = weight -10
		print(self.weight)

h1 =hippo('bob',50)
h1.feed(60)
h1.workout(30)
h1.how_many()




