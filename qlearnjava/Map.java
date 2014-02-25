
import java.util.*;
import javax.swing.*;
import java.awt.*;

public class Map extends JFrame
{
    private State[][] state = new State[Parameter.MAP_SIZE_X][];
    private int currentAgentX;
    private int currentAgentY;
    
    public Map()
    {
        this.currentAgentX = Parameter.START_X;
        this.currentAgentY = Parameter.START_Y;
        
        for(int i = 0; i < Parameter.MAP_SIZE_X; i++)
        {
            state[i] = new State[Parameter.MAP_SIZE_Y];
        }
        
        for(int i = 0; i < Parameter.MAP_SIZE_X; i++)
        {
            for(int j = 0; j < Parameter.MAP_SIZE_Y; j++)
            {
                int kind = Parameter.MAP_DATA[j][i];
                state[i][j] = new State(kind);
                state[i][j].setOpaque(true);
            }
        }
        state[0][1].setReward(100);
        for(int i = 0; i < Parameter.MAP_SIZE_X; i++)
        {
            for(int j = 0; j < Parameter.MAP_SIZE_Y; j++)
            {
                this.setAutoPossibility(i, j);
            }
        }
        
        this.setSize(300,300);
        this.setLayout(new GridLayout(Parameter.MAP_SIZE_X, Parameter.MAP_SIZE_Y));
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        for(int j = 0; j < Parameter.MAP_SIZE_X; j++)
        {
            for(int i = 0; i < Parameter.MAP_SIZE_Y; i++)
            {
                this.add(state[i][j]);
            }
        }
        this.setVisible(true);
    }
    
    public void setCurrentPosition(int x, int y)
    {
        this.currentAgentX = x;
        this.currentAgentY = y;
    }
    
    public void setAutoPossibility(int x, int y)
    {
        for(int i = 0; i < 4; i++)
        {
            state[x][y].setAction(i, true);
        }
        
        for(int i = -1; i <= 1; i++)
        {
            for(int j = -1; j <= 1; j++)
            {
                if(x+i >= 0 && y+j >= 0 && x+i <= Parameter.MAP_SIZE_X-1 && y+j <= Parameter.MAP_SIZE_X-1)
                {
                    if(state[x+i][y+j].getKind() == 3)//もし壁なら
                    {
                        if(i == -1 && j == 0)
                        {
                            state[x][y].setAction(0, false);
                        }
                        else if(i == 1 && j == 0)
                        {
                            state[x][y].setAction(1, false);
                        }
                        else if(i == 0 && j == -1)
                        {
                            state[x][y].setAction(2, false);
                        }
                        else if(i == 0 && j == 1)
                        {
                            state[x][y].setAction(3, false);
                        }
                    }
                }
                else
                {
                    if(x+i < 0)
                        state[x][y].setAction(0, false);
                    if(x+i > Parameter.MAP_SIZE_X-1)
                        state[x][y].setAction(1, false);
                    if(y+j < 0)
                        state[x][y].setAction(2, false);
                    if(y+j > Parameter.MAP_SIZE_Y-1)
                        state[x][y].setAction(3, false);
                }
            }
        }
    }
    
    public State selectState(int x, int y)
    {
        return state[x][y];
    }
    
    public void showMap()
    {
        for(int j = 0; j < Parameter.MAP_SIZE_Y; j++)
        {
            for(int i = 0; i < Parameter.MAP_SIZE_X; i++)
            {
                if(state[i][j].getKind() == 0)
                {
                    System.out.print("S" + " ");
                    state[i][j].setText("  S");
                }
                else if(state[i][j].getKind() == 1)
                {
                    System.out.print("G" + " ");
                    state[i][j].setText("  G");
                }
                else if(state[i][j].getKind() == 2)
                {
                    System.out.print("□" + " ");
                }
                else if(state[i][j].getKind() == 3)
                {
                    System.out.print("■" + " ");
                    state[i][j].setBackground(Color.BLACK);
                    state[i][j].setOpaque(true);
                }
            }
            System.out.println();
        }
        System.out.println();
    }
    
    public void showDirection()
    {
        for(int j = 0; j < Parameter.MAP_SIZE_Y; j++)
        {
            for(int i = 0; i < Parameter.MAP_SIZE_X; i++)
            {
                if(i == currentAgentX && j == currentAgentY)
                {
                    //System.out.print("○ ");
                    state[i][j].setText(" ○");
                    state[i][j].setBackground(Color.BLUE);
                }
                else if(state[i][j].getKind() != 1 && state[i][j].getKind() != 3 && state[i][j].getKind() != 0)
                {
                    double Qvalue = state[i][j].getMaxQvalueAction().getQvalue();
                    if(Qvalue == 0)
                    {
                        //System.out.print("□ ");
                        state[i][j].setText("");
                        state[i][j].setBackground(Color.WHITE);
                    }
                    else if(state[i][j].getMaxQvalueAction().getDirection() == 0)
                    {
                        //System.out.print("← ");
                        state[i][j].setText(" ←");
                        float h = 1;
                        float s = (float)Qvalue/100;
                        if (Qvalue > 99)
                            s = 1;
                        float v = 1;
                        state[i][j].setBackground(new Color(Color.HSBtoRGB(h,s,v)));
                    }
                    else if(state[i][j].getMaxQvalueAction().getDirection() == 1)
                    {
                        //System.out.print("→ ");
                        state[i][j].setText(" →");
                        float h = 1;
                        float s = (float)Qvalue/100;
                        if (Qvalue > 99)
                            s = 1;
                        float v = 1;
                        state[i][j].setBackground(new Color(Color.HSBtoRGB(h,s,v)));
                    }
                    else if(state[i][j].getMaxQvalueAction().getDirection() == 2)
                    {
                        //System.out.print("↑ ");
                        state[i][j].setText(" ↑");
                        float h = 1;
                        float s = (float)Qvalue/100;
                        if (Qvalue > 99)
                            s = 1;
                        float v = 1;
                        state[i][j].setBackground(new Color(Color.HSBtoRGB(h,s,v)));
                    }
                    else if(state[i][j].getMaxQvalueAction().getDirection() == 3)
                    {
                        //System.out.print("↓ ");
                        state[i][j].setText(" ↓");
                        float h = 1;
                        float s = (float)Qvalue/100;
                        if (Qvalue > 99)
                            s = 1;
                        float v = 1;
                        state[i][j].setBackground(new Color(Color.HSBtoRGB(h,s,v)));
                    }
                    else
                    {
                        //System.out.print("□ ");
                        state[i][j].setText("");
                        state[i][j].setBackground(Color.WHITE);
                    }
                }
                else if(state[i][j].getKind() == 3)
                {
                    //System.out.print("■ ");
                    state[i][j].setText("");
                    state[i][j].setBackground(Color.BLACK);
                }
                else if(state[i][j].getKind() == 1)
                {
                    //System.out.print("G ");
                    state[i][j].setText(" G");
                    state[i][j].setBackground(Color.WHITE);
                }
                else if(state[i][j].getKind() == 0)
                {
                    //System.out.print("S ");
                    state[i][j].setBackground(Color.WHITE);
                    state[i][j].setText(" S");
                }
            }
            // System.out.println();
        }
        // System.out.println();
    }
}















