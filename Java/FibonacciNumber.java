class Solution {
    public int fib(int n) {
        
        int prevPrevNum = 0;
        int prevNum = 1;
        
        if(n == 0)
        {
            return 0;
        }
        
        if(n == 1)
        {
            return 1;
        }
        
        int currNum;
        
        for(int i=2; i < n+1; i++)
        {
            currNum = prevNum + prevPrevNum;
            prevPrevNum = prevNum;
            prevNum = currNum;
        }
        
        return prevNum;
    }
}