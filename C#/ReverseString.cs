public class ReverseStringClass {
    /// <summary>
    /// Write a function that reverses a string. The input string is given as an array of characters s.
    /// You must do this by modifying the input array in-place with O(1) extra memory.
    /// Stack approach
    /// Speed: O(N^2)
    /// Space: O(1) but smashes input variable
    /// </summary>
    public void ReverseString(char[] s) {
        Stack<char> charStack = new Stack<char>();
        
        int sLen = s.Length;

        //iterate thru char arr
        for(int i = 0; i < sLen; i++ )
        {
            //push each char onto stack
            charStack.Push(s[i]);
        }
        
        //iterate thru char arr
        for(int i = 0; i < sLen; i++ )
        {
            //pop each char off stack to og string
            s[i] = charStack.Pop();
        }
    }

    /// <summary>
    /// Write a function that reverses a string. The input string is given as an array of characters s.
    /// You must do this by modifying the input array in-place with O(1) extra memory.
    /// Two pointer approach
    /// Speed: O(N)
    /// Space: O(1)
    /// </summary>
    public void ReverseStringSol(char[] s) {
        int l = 0;
        int r = s.Length - 1;

        char ph;
        
        while( l < r)
        {

            //Swap left and right char
            ph = s[l];
            s[l] = s[r];
            s[r] = ph;

            l++;
            r--;
        }
    }
}