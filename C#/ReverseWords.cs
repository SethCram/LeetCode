/*
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Constraints:
1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
*/
public class ReverseWordsClass {
    /// <summary>
    /// Summary: Reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
    /// Approach: Push each word onto the stack, then pop it off into a new char array to reverse ordering since strings immutable.
    ///     After each word, insert a whitespace char if end of string not reached.
    /// </summary>
    /// <param name="s">String s to be reversed.</param>
    /// <returns>Reversed order of chars preserving initial word order.</returns>
    public string ReverseWords(string s) {
        Stack<char> charStack = new Stack<char>();

        char delimiter = ' ';
        
        int sLen = s.Length;

        int sIndex = 0;

        char[] reversedCharArr = new char[sLen];

        //while haven't gone thru whole sentence
        while(sIndex < sLen)
        {

            //iterate thru char arr til hit white space or reach the end
            for(int i = sIndex; i < sLen && s[i] != delimiter; i++ )
            {
                //push each char onto stack
                charStack.Push(s[i]);
            }
            
            //iterate thru char arr til hit white space or reach the end using actual overall index
            while(sIndex < sLen && s[sIndex] != delimiter)
            {
                //pop each char off stack to og string
                reversedCharArr[sIndex] = charStack.Pop();
                sIndex++;
            }
            
            //if haven't hit end of index
            if(sIndex < sLen)
            {
                //insert delimiter into new arr
                reversedCharArr[sIndex] = delimiter;
                sIndex++;
            }

        }
        
        return new string(reversedCharArr);
    }
}