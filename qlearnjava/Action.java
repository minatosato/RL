import java.util.*;

public class Action
{
    private double Qvalue;
    private boolean possibility;
    
    public Action(boolean possibility)
    {
        this.Qvalue = 0;
        this.possibility = possibility;
    }
    
    public double getQvalue()
    {
        return this.Qvalue;
    }
    
    public boolean getPossibility()
    {
        return this.possibility;
    }
    
    public void setPossibility(boolean possibility)
    {
        this.possibility = possibility;
    }
    
    public void updateQvalue(State state)
    {
        double alpha = Parameter.LEARNING_RATE;
        double gamma = Parameter.DISCOUNT_RATE;
        double r = (double)state.getReward();
        double maxQ = state.getMaxQvalueAction().getQvalue();
        
        Qvalue = Qvalue + alpha * (r + gamma * maxQ - Qvalue);
    }
}