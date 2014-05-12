from mandelbrot import Mandelbrot, Scalar, Complex

px = 100
py = 100
dp = 32
cx = Scalar(-1,0) # -1.0
cy = Scalar(3,-1) #  0.3
w  = Scalar(1,-1) #  0.1
h  = w.clone()
fn = "spiralarm-{0}x{1}x{2}.png".format(px,py,dp)

pos = Complex(cx,cy)
man = Mandelbrot()
man.setPosition(pos)
man.setWindowSize(w,h)
man.setPixels(px,py)
man.render(dp)
man.write(fn)
