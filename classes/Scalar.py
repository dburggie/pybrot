
zero = Scalar(0,0)

class Scalar:
	
	def __init__(self, mantissa, exponent):
		self._m = mantissa
		self._e = exponent
	
	def clone(self):
		return Scalar(self._m, self._e)
	
	def copy(self, s):
		self._m = s._m
		self._e = s._e
	
	def __mul__( s, t ):
		return Scalar( s._m * t._m, s._e + t._e )
	
	def __add__( s, t ):
		if (s._e > t._e):
			e = s._e - t._e
			m = s._m * (2 ** e)
			m += t._m
			e = s._e
		else:
			e = t._e - s._e
			m = t._m * (2 ** e)
			m += s._m
			e = t._e
		return Scalar(m,e)
	
	def multiplyBy(self, s):
		self._m *= s._m
		self._e += s._e
	
	def halve(self):
		self._e -= 1
	
	def divide(self, d, precision = 16):
		e = self._e - precision
		m = self._m * 2 ** precision
		m /= d
		while (m % 2 == 0):
			m /= 2
			e += 1
		self._m = m
		self._e = e
	
	def negate(self):
		self._m *= -1
	
	def scale(self, s):
		self._m *= s
	
	def addBy(self, s):
		if (self._e > s._e):
			self._m *= 2 ** (self._e - s._e)
			self._m += s._m
			self._e = s._e
		else:
			m += s._m * (2 ** s._e - self._e)
	
	def size(self):
		return self._m * (2.0 ** self._e)
		
	
