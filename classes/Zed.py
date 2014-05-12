from Scalar import Scalar
from Complex import Complex

zero   = Scalar(0,0)	
origin = Complex( zero, zero )

class Zed:
	
	def __init__(self):
		self.position = origin.clone()
		self.iterator = self.position.clone()
		self.generation = 1
		self.escaped = False
	
	def refresh(self, position):
		self.position.copy(position)
		self.iterator.copy(self.position)
		self.generation = 1
		self.escaped = False
		self.hasEscaped()
	
	def iterate(self):
		if (not self.escaped):
			self.iterator.square()
			self.iterator.addBy(self.position)
			self.generation += 1
		return self.hasEscaped()
	
	def hasEscaped(self):
		if (not self.escaped):
			if (self.iterator.magnitude() > 4.0):
				print "escaped at generation", self.generation
				self.escaped = True
		return self.escaped
