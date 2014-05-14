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
	
	public void refresh(Complex p)
	{
		position.copy(p);
		iteration.copy(position);
		generation = 1;
		bound = true;
		hasEscaped();
	}
	
	public void iterate()
	{
		if (bound)
		{
			iteration.square();
			iteration.addBy(position);
			generation += 1;
		}
		
		return hasEscaped();
	}
	
	public boolean hasEscaped()
	{
		if (bound)
		{
			if (iteration.magnitude() > 4.0)
			{
				bound = false;
			}
		}
		
		return bound;
	}
}
