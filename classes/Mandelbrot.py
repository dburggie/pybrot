from Zed import Zed
from pypng import Png

class Mandelbrot:
	
	def __init__(self):
		self.width = 4.0
		self.height = 4.0
		self.x = 0.0
		self.y = 0.0
		self.getWindowCorners()
		
		self.resolved = False
		self.xPix = 0
		self.yPix = 0
		
		self.rendered = False
		self.image = None
	
	def setResolution(self, xPix, yPix):
		self.xPix = xPix
		self.yPix = yPix
		self.resolved = True
	
	def setWindowSize(self, width, height):
		self.width = width
		self.height = height
		self.getWindowCorners()
	
	def setWindowPosition(self, x, y):
		self.x = x
		self.y = y
		self.getWindowCorners()
	
	def getWindowCorners(self):
		hw = self.width / 2.0
		hh = self.height / 2.0
		self.x0 = self.x - hw
		self.x1 = self.x + hw
		self.y0 = self.y - hh
		self.y1 = self.y + hh
	
	def render(self, depth = 16):
		if (self.rendered):
			return True
		self.image = Png(self.xPix,self.yPix)
		xStep = self.width / self.xPix
		yStep = self.height / self.yPix
		xPos = self.x0
		yPos = self.y0
		
		z = Zed(0.0,0.0)
		
		y = 0
		while (y < self.yPix):
			x = 0
			xPos = self.x0
			while (x < self.xPix):
				z.refresh(xPos,yPos)
				c = 0
				while (z.bound and c < depth):
					z.iterate()
					c += 1
				self.image.set_pixel(x,y,z.colorize(depth))
				x += 1
				xPos += xStep
			y += 1
			yPos += yStep
		self.rendered = True
		return False
	
	def write(self, filename):
		if (self.rendered):
			self.image.write(filename)
	
	
	
	
	
	
	
