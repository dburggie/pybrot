
_precision = 72
_maxMantissa = 2 ** 64
_clipbits = 8
_clipvalue = 2 ** _clipbits



	
class Scalar:
	
	def setGlobalPrecision(p):
		_precision = p + _clipbits
		_maxMantissa = 2 ** p
	
	def _strip(self):
		count = 0
		while ( abs(self._m) > self._mm ):
			self._m /= _clipvalue
			self._e += _clipbits
			count += 1
		return count
	
	
	
	def __init__(self, m = None, e = None, decimal = True):
		if (not e):
			self._m = 0
			self._e = 0
			self._p = _precision
			self._mm = _maxMantissa
			self._strip()
		else:
			self._m = m
			self._e = e
			self._p = _precision
			self._mm = _maxMantissa
			if (decimal):
				self._decToBin()
	
	
	
	def _decToBin(self):
		if (self._e < 0):
			exp = abs(self._e)
			bits = self._p + exp + exp/2
			m = (2 ** bits) / (5 ** exp)
			e = -bits
			s = Scalar(m,e,False)
			s._strip()
			self.multiplyBy(s)
		else:
			self._m *= 5 ** self._e
		self._strip()
		
	
	
	def clone(self):
		return Scalar(self._m, self._e, False)
	
	
	
	def copy(self, s):
		self._m = s._m
		self._e = s._e
	
	
	
	def __mul__( s, t ):
		return Scalar( s._m * t._m, s._e + t._e, False)
	
	def __add__( s, t ):
		diff = abs(s._e - t._e)
		if (s._e > t._e):
			m = s._m * (2 ** diff)
			m += t._m
			e = s._e
		else:
			m = t._m * (2 ** diff)
			m += s._m
			e = t._e
		return Scalar(m,e,False)
	
	
	
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
			self._m += s._m * (2 ** (s._e - self._e) )
		self._strip()
	
	def size(self):
		return self._m * (2.0 ** self._e)
		
	
