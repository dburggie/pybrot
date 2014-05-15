package dburggie.mandelbrot;

import dburggie.imageutils.*;

public class Mandelbrot
{
	
	private Complex position;
	private double width, height;
	private int xPixels, yPixels;
	private int depth;
	
	public Mandelbrot()
	{
		
		position = new Complex(0.0,0.0);
		width = 4.0; height = 4.0;
		xPixels = 0; yPixels = 0;
		depth = 32;
		
	}
	
	public void setPosition(double x, double y)
	{
		position.setXY(x,y);
	}
	
	public void setWindow(double w, double h)
	{
		if (w > 0 && h > 0)
		{
			width = w;
			height = h;
		}
	}
	
	public void setResolution(int xp, int yp)
	{
		if (xp > 0 && yp > 0)
		{
			xPixels = xp; yPixels = yp;
		}
		
		else
		{
			xPixels = 0; yPixels = 0;
		}
	}
	
	public void setDepth(int d)
	{
		if (d > 0)
		{
			depth = d;
		}
		
		else
		{
			depth = 0;
		}
	}
	
	private boolean verify()
	{
		boolean error = false;
		if (depth <= 0)
		{
			error = true;
		}
		if (xPixels <= 0 || yPixels <= 0)
		{
			error = true;
		}
		if (width < 0.0 || height < 0.0)
		{
			error = true;
		}
		return error;
	}
	
	public boolean render()
	{
		return render(2.0);
	}
	
	public boolean render(String filename)
	{
		return render(filename, 2.0);
	}
	
	public boolean render(double power)
	{
		String filename = "mandelbrot-";
		filename += xPixels + "x" + yPixels;
		filename += "x" + depth + ".png";
		return render(filename, power);
	}
	
	public boolean render(String filename, double power)
	{
		if (verify())
		{
			return true;
		}
		
		
		Complex pos = new Complex(-width,height);
		pos.scale(0.5);
		pos.addBy(position);
		
		double x0 = pos.getRealPart();
		Complex dx = new Complex(width / xPixels, 0.0);
		Complex dy = new Complex(0.0, -1.0 * height / yPixels);
		
		
		Zed tracker = new Zed();
		Colorizer color = new Colorizer();
		MyImage image = new MyImage(xPixels, yPixels);
		
		for (int y = 0; y < yPixels; y++)
		{
			pos.setRealPart(x0);
			for (int x = 0; x < xPixels; x++)
			{
				tracker.refresh(pos);
				tracker.iterate(depth);
				image.setPixel(x,y,color.colorize(tracker,depth,power));
				pos.addBy(dx);
			}
			pos.addBy(dy);
		}
		
		image.write(filename);
		return false;
	}
	
	
	
	public static void main(String [] args)
	{
		double xpos, ypos, width, power;
		int pixels, depth;
		
		try
		{
			
			if (args.length < 5 || args.length > 6)
			{
				throw new Exception();
			}
			
			xpos = Double.parseDouble(args[0]);
			ypos = Double.parseDouble(args[1]);
			width = Double.parseDouble(args[2]);
			pixels = Integer.decode(args[3]);
			depth = Integer.decode(args[4]);
			if (args.length == 6) { power = Double.parseDouble(args[5]); }
			else { power = 2.0; }
			
		}
		
		catch (Exception e)
		{
			System.out.println("Error parsing arguments: using defaults.");
			System.out.println("Usage: Mandelbrot x y width pixels depth");
			xpos = 0.0; ypos = 0.0; width = 4.0; power = 2.0;
			pixels = 400; depth = 32;
		}
		
		Mandelbrot man = new Mandelbrot();
		man.setPosition(xpos,ypos);
		man.setWindow(width,width);
		man.setResolution(pixels,pixels);
		man.setDepth(depth);
		man.render(power);
		
	}
	
}
