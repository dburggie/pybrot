package dburggie.mandelbrot;

import dburggie.imageutils.MyColor;

public class Colorizer extends MyColor
{
	
	public Colorizer() { super(); }
	
	public MyColor colorize(Zed zed, int depth)
	{
		return colorize(zed,depth,2.0);
	}
	
	public MyColor colorize(Zed zed, int depth, double power)
	{
		
		int speed = zed.speed();
		double rate = 1.0, rg = 0.0, b = 0.0;
		if (speed > 0)
		{
			rate = ( 1.0 * speed ) / (depth - 1);
			//System.out.println("Speed: " + speed + " Rate: " + rate);
			rg = 0.7 * Math.pow(rate, power);
			b = 0.3 + 0.7 * rate;
		}
		
		return setRGB(rg,rg,b);
	}
}
