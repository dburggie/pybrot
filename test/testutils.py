from mandelbrot import Scalar, Complex
from random import randint

rmin = -100
rmax = 100

def rnd():
	return randint(rmin,rmax)

def closeTo(a, b):
	if ( abs(a - b) < 0.01 ):
		return True
	return False

def getS():
	return Scalar(rnd(),rnd())

def getZ():
	return Complex(getS(),getS())
	
