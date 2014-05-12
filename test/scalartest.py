from mandelbrot import Scalar

s = Scalar(12345, -5)
print "mantissa:", s._m, "exponent:", s._e
print s.size(), "should be 0.12345"
