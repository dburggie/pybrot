package dburggie.mandelbrot;

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
	
	public void setXY(double x, double y)
	{
		rp = x; ip = y;
	}
	
	public void setRealPart(double x)
	{
		rp = x;
	}
	
	public double getRealPart() { return rp; }
	public double getImagPart() { return ip; }
	
	
	
	public void copy(Complex c)
	{
		rp = c.rp;
		ip = c.ip;
	}
	
	public void addBy(Complex c)
	{
		rp += c.rp; ip += c.ip;
	}
	
	public void scale(double s)
	{
		rp *= s; ip *= s;
	}
	
	public void multiplyBy(Complex c)
	{
		double r = rp, i = ip;
		rp = r * c.rp - i * c.ip;
		ip = r * c.ip + i * c.rp;
	}
	
	public void square()
	{
		double r = rp, i = ip;
		rp = r * r - i * i;
		ip = 2 * r * i;
	}
	
	public double magnitude()
	{
		return rp * rp + ip * ip;
	}
	
}
