#include <iostream>
#include <stack>
#include <vector> //need to us []
using namespace std;

class Solution {
public:
    //doesn't work likely bc of null character detection not working properly (can't index arr past reg space unless in C?)
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

int main()
{
    Solution solution;

    vector<char> charVector; //{'h', 'e', 'l', 'l', 'o'};

    charVector.push_back('h');
    charVector.push_back('e');
    charVector.push_back('l');
    charVector.push_back('l');
    charVector.push_back('o');

    solution.reverseString(charVector);

    //cout << (string)charVector;

    cout << "end of main";

    return 0;
}