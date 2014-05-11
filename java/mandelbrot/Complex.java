package mandelbrot;

public class Complex
{
	
	private Scalar realPart;
	private Scalar imaginaryPart;
	
	public Complex( Complex c )
	{
		copy(c);
	}
	
	public Complex( Scalar r, Scalar i )
	{
		realPart = r.clone();
		imaginaryPart = i.clone();
	}
	
	public Scalar clone()
	{
		return new Complex(realPart, imaginaryPart);
	}
	
	public void copy(Complex c)
	{
		realPart.copy(c.realPart);
		imaginaryPart.copy(c.imaginaryPart);
	}
	
	public void addBy(Complex c)
	{
		realPart.addBy(c.realPart);
		imaginaryPart.addBy(c.imaginaryPart);
	}
	
	public void multiplyBy(Complex c)
	{
		Complex real = realPart.clone();
		Complex imag = imaginaryPart.clone();
		
		realPart.multiplyBy(c.realPart); // now r * cr
		imag.multiplyBy(c.imaginaryPart); // now i * ci
		imag.multiplyBy(-1); // now -i * ci
		realPart.addBy(imag); // now r*cr-i*ci
		
		imaginaryPart.multiplyBy(c.realPart); //now i*cr
		real.multiplyBy(c.imaginaryPart); // now r*ci
		imaginaryPart.addBy(real); //now r*ci+i*cr
	}
	
	public double magnitude()
	{
		double r = realPart.size();
		double i = imaginaryPart.size();
		return r*r + i*i
	}
	
}
