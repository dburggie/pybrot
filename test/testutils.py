from mandelbrot import Scalar, Complex
from random import randint

rmin = -10
rmax = 5

def rnd():
	return randint(rmin,rmax)

def closeTo(a, b):
	if ( abs(a - b) < 0.1 * min(a,b) ):
		return True
	return False

def getS():
	return Scalar(rnd(),rnd())

def getZ():
	return Complex(getS(),getS())
	
