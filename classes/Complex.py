

class Complex:
	
	def fromDouble(d):
		
		exp = 0
		
		if (d < 0):
			d *= -1
			negate = True
		else:
			negate = False
		
		while (d > (int) d):
			d *= 2
			exp -= 1
		
	
	def __init__(self, r, i):
		self.r = r.clone()
		self.i = i.clone()
	
	def clone(self):
		return Complex(self.r, self.i)
	
	def copy(self, c):
		self.r.copy(c.r)
		self.i.copy(c.i)
	
	def __mul__(self, c):
		r = self.r * c.r - self.i * c.i
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
	
	def addBy(self, c):
		self.r.addBy(c.r)
		self.i.addBy(c.i)
	
	def addXY(self, dx, dy):
		self.r.addBy( dx )
		self.i.addBy( dy )
	
