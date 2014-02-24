
import java.util.*;
import javax.swing.*;
import java.awt.*;

public class State extends JLabel
{
    private Action[] action = new Action[4];
    private int reward;
    private int kind;
    private int direction;
    
    public State(int kind)
    {
        this.reward = 0;
        this.kind = kind;
    }
    
    public void setReward(int reward)
    {
        this.reward = reward;
    }
    
    public int getReward()
    {
        return this.reward;
    }
    
    public int getKind()
    {
        return this.kind;
    }
    
    public void setAction(int direction, boolean possiblility)
    {
        action[direction] = new Action(possiblility);
    }
    
    public Action getMaxQvalueAction()
    {
        int max = 0;
        
        for(int i = 1; i < 4; i++)
        {
            if(action[i].getQvalue() > action[max].getQvalue())
            {
                max = i;
            }
        }
        return action[max];
    }
    
    public int getMaxQvalueActionNumber()
    {
        int max = 0;
        
        for(int i = 1; i < 4; i++)
        {
            if(action[i].getQvalue() > action[max].getQvalue())
            {
                max = i;
            }
        }
        
        if(action[0].getQvalue() == 0 && action[1].getQvalue() == 0 && action[2].getQvalue() == 0 && action[3].getQvalue() == 0)
        {
            max = (new Random()).nextInt(4);
        }
        
        return max;
    }
    
    public Action actionSelect()
    {
        int choosen = 0;
        
        double random = Math.random();
        
        if(random > Parameter.EPSILON_RATE)
        {
            //greedy
            choosen = this.getMaxQvalueActionNumber();
            
            this.direction = choosen;
        }
        else
        {
            //random
            choosen = (new Random()).nextInt(4);
            
            this.direction = choosen;
        }
        return action[choosen];
    }
    
    public int actionSelectNumber()
    {
        return this.direction;
    }
}