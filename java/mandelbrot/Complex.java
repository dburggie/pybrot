package mandelbrot;

public class Complex
{
	
	private double rp, ip;
	
	public Complex( Complex c )
	{
		rp = c.rp; ip = c.ip;
	}
	
	public Complex( double r, double i )
	{
		rp = r; ip = i;
	}
	
	public Complex clone()
	{
		return new Complex(rp,ip);
	}
	
	public void copy(Complex c)
	{
		rp = c.rp;
		ip = c.ip;
	}
	
	public void addBy(Complex c)
	{
		rp += c.rp; ip += c.ip;
	}
	
	public void multiplyBy(Complex c)
	{
		r = rp; i = ip;
		rp = r * c.r - i * c.i;
		ip = r * c.i + i * c.r;
	}
	
	public void square()
	{
		r = rp; i = ip;
		rp = r * r - i * i;
		ip = 2 * r * i;
	}
	
	public double magnitude()
	{
		return rp * rp + ip * ip;
	}
	
}
