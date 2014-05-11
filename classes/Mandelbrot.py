from Scalar import Scalar
from Complex import Complex
from Zed import Zed, zero, origin

from pypng import Png

def colorize(zed, depth, samplemax = 255):
	if (zed.genertion == depth):
		return [0,0,0]
	distance = zed.generation - 1
	distance *= 1.0 / (depth - 1)
	rg = 0.7 * distance ** 2.0
	rg = int(rg * samplemax)
	b = int(distance * samplemax)
	return [rg,rg,b]

_up    = Complex( zero, Scalar( 1, 0) )
_down  = Complex( zero, Scalar(-1, 0) )
_right = Complex( Scalar( 1, 0), zero )
_left  = Complex( Scalar(-1, 0), zero )


class Mandelbrot:
	# Members:
	# 	Complex position
	# 	Scalar width
	# 	Scalar height
	# 	int xPix
	# 	int yPix
	# 	boolean setup
	# 	Png image
	# 	boolean rendered
	
	def __init__(self):
		self.position = origin.clone()
		self.width = Scalar(4, 0)
		self.height = Scalar(4, 0)
		self.xPix = 1
		self.yPix = 1
		self.setup = False
		self.image = Png()
		self.rendered = False
	
	def setPosition(self, position):
		self.position.copy(position)
	
	def setWidth(self, width):
		self.width.copy(width)
	
	def setHeight(self, height:
		self.height.copy(height)
	
	def setWindowSize(self, width, height):
		self.width.copy(width)
		self.height.copy(height)
	
	def setPixels(self, xPix, yPix):
		self.xPix = xPix
		self.yPix = yPix
		setup = True
	
	def render(self, filename = None, depth = 32):
		if (not self.setup):
			print "You need to set up your fractal before you can render it!"
			return True
		
		if (self.rendered):
			print "You've already rendered this!"
			return True

		if (not filename):
			filename = "mandelbrot-{0}x{1}x{2}.png".format(xPix,yPix,depth)
		
		x0 = self.width.clone()
		x0.halve()
		x0.scale(-1)
		x0.addBy(self.position.r)

		y0 = self.height.clone()
		y0.halve()
		y0.addBy(self.position.i)

		xStep = self.width.clone()
		xStep.divide(self.xPix)
		yStep = self.height.clone()
		yStep.negate()
		yStep.divide(self.yPix)

		zed = Zed()
		
		x = 0
		y = 0

		while (y < self.yPix):
			zed.

		
	
	
