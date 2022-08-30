public class ReverseStringClass {
    public void ReverseString(char[] s) {
        Stack<char> charStack = new Stack<char>();
        
        int sLen = s.Length;

        //iterate till hit the null char
        for(int i = 0; i < sLen; i++ )
        {
            //push each char onto stack
            charStack.Push(s[i]);
        }
        
        //iterate till hit the null char
        for(int i = 0; i < sLen; i++ )
        {
            //pop each char off stack to og string
            s[i] = charStack.Pop();
        }
    }
}