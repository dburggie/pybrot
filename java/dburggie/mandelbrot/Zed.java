package dburggie.mandelbrot;

public class Zed
{
	private Complex position;
	private Complex iteration;
	private int generation;
	private boolean bound;
	
	public Zed()
	{
		this( new Complex(0.0,0.0) );
	}
	
	public Zed(Complex p)
	{
		position = p.clone();
		iteration = position.clone();
		generation = 1;
		bound = true;
		hasEscaped();
	}
	
	public void refresh(double x, double y)
	{
		position.setXY(x,y);
		iteration.copy(position);
		generation = 1;
		bound = true;
		hasEscaped();
	}
	
	public void refresh(Complex p)
	{
		position.copy(p);
		iteration.copy(position);
		generation = 1;
		bound = true;
		hasEscaped();
	}
	
	public void iterate(int n)
	{
		for (int i = 0; i < n; i++)
		{
			if (!bound)
			{
				break;
			}
			
			iteration.square();
			iteration.addBy(position);
			hasEscaped();
		}
	}
	
	public int hasEscaped()
	{
		if (bound)
		{
			if (iteration.magnitude() > 4.0)
			{
				bound = false;
				return generation;
			}
			
			return 0;
		}
		
		return generation;
	}
}
