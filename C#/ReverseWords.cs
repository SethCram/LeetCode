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
            for(int i = sIndex; i < sLen && s[i] == delimiter; i++ )
            {
                //push each char onto stack
                charStack.Push(s[i]);
            }
            
            //iterate thru char arr til hit white space or reach the end
            for(int i = sIndex; i < sLen && s[i] == delimiter; i++ )
            {

                //pop each char off stack to og string
                reversedCharArr[i] = charStack.Pop();

                //incr overall placement in s string
                sIndex++;
            }

        }
        
        return new string(reversedCharArr);
    }
}