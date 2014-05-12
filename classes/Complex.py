

class Complex:
	
	def __init__(self, r, i):
		self.r = r.clone()
		self.i = i.clone()
	
	def clone(self):
		return Complex(self.r, self.i)
	
	def copy(self, c):
		self.r.copy(c.r)
		self.i.copy(c.i)
	
	def __mul__(self, c):
		r = self.i * c.i
		r.negate()
		r.addBy(self.r * c.r)
		i = self.r * c.i + self.i * c.r
		return Complex(r,i)
	
	def __add__(self, c):
		n = Complex(self.r, self.i)
		n.r.addBy(c.r)
		n.i.addBy(c.i)
		return n
	
	def __len__(self):
		x = self.r.size()
		y = self.i.size()
		return (x * x + y * y) ** 0.5
	
	def magnitude(self):
		x = self.r.size()
		y = self.i.size()
		return x * x + y * y
		
	def setCoordinates(self, r, i):
		self.r.copy(r)
		self.i.copy(i)
	
	def halve(self):
		self.r.halve()
		self.i.halve()
	
	def pMultiply(self, d, p = 16):
		self.r.pMultiply(d,p)
		self.i.pMultiply(d,p)

	def divide(self, d, p = 16):
		self.r.divide(d,p)
		self.i.divide(d,p)
	
	def scale(self, s):
		self.r.multiplyBy(s)
		self.i.multiplyBy(s)
	
	def multiplyBy(self, c):
		
		r = self.r.clone()
		r.multiplyBy(c.r)
		
		b = self.i.clone()
		b.multiplyBy(c.i)
		b.negate()
		r.addBy(b)
		
		i = self.i.clone()
		i.multiplyBy(c.r)
		b.copy(self.r)
		b.multiplyBy(c.i)
		i.addBy(b)
		
		self.r.copy(r)
		self.i.copy(i)
	
	def square(self):
		# r <- rr - ii
		# i <- 2ri
		i = self.i.clone()
		self.i.multiplyBy(self.r)
		self.i.scale(2)
		self.r.multiplyBy(self.r)
		i.multiplyBy(i)
		i.scale(-1)
		self.r.addBy(i)
	
	def addBy(self, c):
		self.r.addBy(c.r)
		self.i.addBy(c.i)
	
	def addXY(self, dx, dy):
		self.r.addBy( dx )
		self.i.addBy( dy )
	
