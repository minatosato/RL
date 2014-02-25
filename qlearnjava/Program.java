
//import java.util.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Program implements ActionListener
{
    private Map maze;
    private Agent agent;
    private Action a;
    private int a_num;
    private State s;
    private Timer timer;
    
    public Program()
    {
        timer = new Timer(1,this);
        
        maze = new Map();
        
        agent = new Agent();
        
        s = maze.selectState(agent.getCurrentX(), agent.getCurrentY());
        
        timer.start();
        
        maze.showMap();
        
    }
    
    public void actionPerformed(ActionEvent e)
    {
        a = s.actionSelect();

        agent.move(a);
        
        s = maze.selectState(agent.getCurrentX(), agent.getCurrentY());
        
        a.updateQvalue(s);
        
        maze.setCurrentPosition(agent.getCurrentX(), agent.getCurrentY());
        
        maze.showDirection();
        
        if(s.getKind() == 1)
        {
            agent.move();
        }
        
    }

    public static void main(String[] args)
    {
        new Program();
    }
}
