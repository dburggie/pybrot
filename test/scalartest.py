from mandelbrot import Scalar

from testutils import rnd, closeTo

def add():
	errors = ""
	s = Scalar(rnd(),rnd())
	t = Scalar(rnd(),rnd())
	targetsize = s.size() + t.size()
	
	u = (s + t)
	if ( not closeTo(u.size(), targetsize) ):
		errors += "bad result size in Scalar.__add__()\n"
	
	u.copy(s)
	u.addBy(t)
	if ( not closeTo(u.size(), targetsize) ):
		errors += "bad result size in Scalar.addBy()\n"
	
	return errors

def mul():
	errors = ""
	s = Scalar(rnd(),rnd())
	t = Scalar(rnd(),rnd())
	targetsize = s.size() * t.size()
	
	u = (s * t)
	if ( not closeTo(u.size(), targetsize) ):
		errors += "bad result size in Scalar.__mul__()\n"
	
	u.copy(s)
	u.multiplyBy(t)
	if ( not closeTo(u.size(), targetsize) ):
		errors += "bad result size in Scalar.multiplyBy()\n"
	return errors
	
def run(n):
	
	report = ""
	while (n > 1):
		n -= 1
		
		errors = add()
		if len(errors):
			report += "Scalar add errors:\n" + errors
		
		errors = mul()
		if len(errors):
			report += "Scalar mult errors:\n" + errors
		
	print report



