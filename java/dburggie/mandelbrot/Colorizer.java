package dburggie.mandelbrot;

import dburggie.imageutils.MyColor;

public class Colorizer extends MyColor
{
	private int depth;
	
	private Zed zed;
	
	public Colorizer(Zed z, int d)
	{
		zed = z;
		depth = Math.max(2, d);
	}
	
	public void setDepth(int d) { depth = d; }
	
	public MyColor colorize()
	{
		
		int speed = zed.speed(depth);
		double rate = 1.0, rg = 0.0, b = 0.0;
		if (speed > 0)
		{
			rate = ( (double) speed ) / (depth - 1);
			rg = 0.7 * rate * rate;
			b = 0.3 + 0.7 * rate;
		}
		
		return setRGB(rg,rg,b);
	}
}
