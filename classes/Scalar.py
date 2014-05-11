
_precision = 64
_maxMantissa = 2 ** 64

class Scalar:
	
	def setGlobalPrecision(p):
		_precision = p
		_maxMantissa = 2 ** p
	
	def _strip(self):
		while (self._m % 2 == 0):
			self._m /= 2
			self._e += 1
		while ( abs(self._m) > self._mm ):
			print self._m, self._mm
			self._m /= 2
			self._e += 1
	
	def __init__(self, mantissa, exponent):
		self._m = mantissa
		self._e = exponent
		self._p = _precision
		self._mm = _maxMantissa
		if (self._m):
			self._strip()
	
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
	
	def pMultiply(self, d, p = 16):
		m = self._m * 2 ** p
		m = int(m * d)
		e = self._e - p
		self._m = m
		self._e = e
		self._strip()

	def multiplyBy(self, s):
		self._m *= s._m
		self._e += s._e
		self._strip()
	
	def halve(self):
		self._e -= 1
	
	def divide(self, d, p = 16):
		e = self._e - p
		m = self._m * 2 ** p
		m = int(m / d)
		self._m = m
		self._e = e
		self._strip()
	
	def negate(self):
		self._m *= -1
	
	def scale(self, s):
		self._m *= s
		self._strip
	
	def addBy(self, s):
		if (self._e > s._e):
			self._m *= 2 ** (self._e - s._e)
			self._m += s._m
			self._e = s._e
		else:
			self._m += s._m * (2 ** s._e - self._e)
		self._strip()
	
	def size(self):
		return self._m * (2.0 ** self._e)
		
	
