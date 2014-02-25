
import java.util.*;

public class Agent
{
    private int currentX;
    private int currentY;
    
    public Agent()
    {
        this.currentX = Parameter.START_X;
        this.currentY = Parameter.START_Y;
    }
    
    public int getCurrentX()
    {
        return this.currentX;
    }
    
    public int getCurrentY()
    {
        return this.currentY;
    }
    
    public void move(Action action)
    {
        boolean possibility = action.getPossibility();
        int direction = action.getDirection();
        
        if(direction == 0 && possibility == true)
        {
            currentX--;
        }
        else if(direction == 1 && possibility == true)
        {
            currentX++;
        }
        else if(direction == 2 && possibility == true)
        {
            currentY--;
        }
        else if(direction == 3 && possibility == true)
        {
            currentY++;
        }
    }
    
    public void move()
    {
        currentX = Parameter.START_X;
        currentY = Parameter.START_Y;
    }
}