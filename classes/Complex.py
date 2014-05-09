

class Complex:
	
	def __init__(self, r, i):
		self.r = r
		self.i = i
	
	def __mul__(self, c):
		r = self.r * c.r - self.i * c.i
		i = self.r * c.i + self.i * c.r
		return Complex(r,i)
	
	def __add__(self, c):
		r = self.r + c.r
		i = self.i + c.r
		return Complex(r,i)
	
	def __len__(self):
		return (self.r * self.r + self.i * self.i) ** 0.5
	
	def setCoordinates(self, r, i):
		self.r = r
		self.i = i
	
	def multiplyBy(self, c):
		r = self.r * c.r - self.i * c.i
		i = self.r * c.i + self.i * c.r
		self.r = r
		self.i = i
	
	def add(self, c):
		self.r += c.r
		self.i += c.i
	
	def addXY(self, x, y):
		self.r += x
		self.i += y
	
	def magnitude(self):
		return self.r * self.r + self.i * self.i
	
	def copy(self, c):
		self.r = c.r
		self.i = c.i
	
	def clone(self):
		return Complex(self.r, self.i)
