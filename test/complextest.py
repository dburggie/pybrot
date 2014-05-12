from mandelbrot import Complex
from testutils import closeTo, getZ

def add():
	
	report = ""
	
	x = getZ()
	y = getZ()
	
	dx = x.r.size() + y.r.size()
	dy = x.i.size() + y.i.size()
	distance = (dx * dx + dy * dy)
	
	z = x + y
	if not closeTo(z.magnitude(), distance):
		report += "bad result size in Complex.__add__()\n"
	
	z.copy(x)
	z.addBy(y)
	if not closeTo(z.magnitude(),distance):
		report += "bad result size in Complex.addBy()\n"
	
	return report

def mul():
	
	report = ""
	
	x = getZ()
	y = getZ()
	
	distance = x.magnitude() * y.magnitude()
	
	z = x * y
	if not closeTo(z.magnitude(), distance):
		report += "bad result size in Complex.__mul__()\n"
	
	z.copy(x)
	z.multiplyBy(y)
	if not closeTo(z.magnitude(),distance):
		report += "bad result size in Complex.multiplyBy()\n"
	
	return report

def run(n):
	
	report = ""
	while n > 1:
		n -= 1
		errors = add()
		if len(errors):
			report += "Complex add errors:\n" + errors
		
		errors = mul()
		if len(errors):
			report += "Complex multiply errors:\n" + errors
	
	print report



