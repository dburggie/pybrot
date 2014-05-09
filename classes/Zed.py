from Complex import Complex

class Zed:
	
	def __init__(self, x, y):
		self.c = Complex(x, y)
		self.n = 1
		self.z = self.c.clone()
		self.bound = True
		self.isBound()
	
	def isBound(self):
		if (self.z.magnitude() > 4.0):
			self.bound = False
#			print "z went out of bounds after", 
#			print self.n, "iterations", 
#			print "z:", self.z.r, "+ i *", self.z.i,
#			print "c:", self.c.r, "+ i *", self.c.i
	
	def iterate(self):
		if (self.bound):
			self.z.multiplyBy(self.z)
			self.z.add(self.c)
			self.n += 1
			self.isBound()
	
	def refresh(self, xPos, yPos):
		self.c.setCoordinates(xPos, yPos)
		self.n = 1
		self.z.copy(self.c)
		self.bound = True
		self.isBound()
	
	def colorize(self, depth, sampleMax = 255):
		if (self.bound):
			return [0,0,0]
		ratio = float(depth - self.n) / (depth - 1)
		rg = int(sampleMax * (ratio ** 2.0))
		b = sampleMax
		return [ rg,rg,b ]
		
		
			
	
