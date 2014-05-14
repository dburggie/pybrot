package dburggie.mandelbrot;

public class Scalar
{
	
	private long mantissa;
	private long exponenet;
	
	public Scalar( Scalar s ) { copy(s); }
	public Scalar( long m, long e ) { mantissa = m; exponent = e; }
	
	public void copy( Scalar s )
	{
		mantissa = s.mantissa;
		exponent = s.exponent;
	}
	
	public Scalar clone()
	{
		return new Scalar(mantissa,exponent);
	}
	
	public void multiplyBy(Scalar s)
	{
		mantissa *= s.mantissa;
		exponent += s.exponent;
	}
	
	public void multiplyBy(int i)
	{
		matissa *= i;
	}
	
	public static Scalar add(Scalar a, Scalar b)
	{
		long m, e;
		if (a.exponent > b.exponent)
		{
			e = a.exponent - b.exponent;
			m = a.mantissa * Math.pow(2, e);
			m += b.mantissa;
			e = b.exponent;
		}
		
		else
		{
			e = b.exponent - a.exponent;
			m = b.mantissa * Math.pow(2,e);
			m += a.mantissa;
			e = a.exponent;
		}
		
		return new Scalar(m,e);
	}
	
	public static Scalar max(Scalar a, Scalar b)
	{
		if (a.lessThan(b))
		{
			return b;
		}
		
		else
		{
			return a;
		}
	}
	
	public boolean lessThan(Scalar s)
	{
		if (exponent < s.exponent)
		{
			return true;
		}
		
		else if (exponent < s.exponent)
		{
			return false;
		}
		
		else if (mantissa < s.mantissa)
		{
			return true;
		}
		
		else
		{
			return false;
		}
	}
	
	public void addBy(Scalar s)
	{
		long m, e;
		if (exponent > s.exponent)
		{
			e = exponent - s.exponent;
			m = mantissa * Math.pow(2, e);
			m += s.mantissa;
			mantissa = m; exponent = s.exponent;
		}
		
		else
		{
			e = s.exponent - exponent;
			m = s.mantissa * Math.pow(2,e);
			m += mantissa;
			mantissa = m;
		}
	}
	
	public double size()
	{
		return mantiss * Math.pow(2.0, exponent);
	}
}
