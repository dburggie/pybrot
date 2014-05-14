package dburggie.mandelbrot;

public class Mandelbrot
{
	private static final Scalar zero = new Scalar(0L,0L);
	
	private Complex position;
	private Complex iteration;
	private int generation;
	private boolean escaped;
	
	public Mandelbrot()
	{
		position = new Complex(zero, zero);
		iteration = position.clone();
		generation = 1;
		escaped = false;
		hasEscaped();
	}
	
	public void refresh(Complex newPosition)
	{
		position.copy(newPosition);
		iteration.copy(position);
		generation = 1;
		escaped = false;
		hasEscaped();
	}
	
	public boolean iterate()
	{
		if (escaped)
		{
			return true;
		}
		
		iteration.square();
		iteration.addBy(position);
		generation += 1;
		return hasEscaped();
	}
	
	public boolean hasEscaped()
	{
		if (!escaped)
		{
			if (iteration.magnitude() > 4.0)
			{
				escaped = true;
			}
		}
		
		return escaped;
	}
	
	public int getGen() { return generation; }
	
}
