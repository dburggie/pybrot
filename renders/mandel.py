from mandelbrot import Mandelbrot, Scalar, Complex

px = 10
py = 10
dp = 32
cx = Scalar(10,0) # -1.0
cy = Scalar(10,0) #  0.3
w  = Scalar(4,0) #  0.1
h  = w.clone()
fn = "mandelbrot-{0}x{1}x{2}.png".format(px,py,dp)

pos = Complex(cx,cy)
man = Mandelbrot()
man.setPosition(pos)
man.setWindowSize(w,h)
man.setPixels(px,py)
man.render(dp)
man.write(fn)
