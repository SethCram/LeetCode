#include <iostream>
#include <stack>
using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) // & = pass by ref
    {
        //could use a stack to push all, then pop all
        
        //int strLen = s.Length();
        
        //use C++ to use STL
        stack<char> charStack;
        
        //iterate till hit the null char
        for(int i = 0; s[i] != '\0'; i++ )
        {
            //push each char onto stack
            charStack.push(s[i]);
        }
        
        //iterate till hit the null char
        for(int i = 0; s[i] != '\0'; i++ )
        {
            //pop each char off stack to og string
            s[i] = charStack.top();
            charStack.pop();
        }
        
    }
};