/// @brief 
class Solution {
public:
    /// @brief Failed iterative attempt.
    /// @param s 
    /// @return 
    string decodeString(string s) {
        
        int substrEndIndex;
        int substrStartIndex;
        
        string iterationsStr = "";
        
        string output = "";
        
        string entireOutputStr = "";
        
        int withinBrackets = 0;
        
        //bool betweenBrackets = false;
        bool digitPreviouslySeen = false;
        
        //walk thru s backwards
        for(int sPtr=s.length()-1; sPtr >= 0; sPtr--)
        {
            bool isDigit = isdigit(s[sPtr]);
            
            //if digit
            if(isDigit)
            {
                digitPreviouslySeen = true;
                
                iterationsStr = s[sPtr] + iterationsStr;
                
            }
            
            //if no more digits but one previously seen, or digit is first elly in str
            if((digitPreviouslySeen && !isDigit) || (sPtr == 0 && isDigit))
            {
                //printf("%d, %d", substrEndIndex, substrStartIndex );
                
                int substrLen = substrEndIndex-substrStartIndex+1;
                
                string subStr = s.substr(substrStartIndex, substrLen) + output;
                
                output = "";
                //conv str to int
                int iterationsNum = stoi(iterationsStr);
                
                //cout << "before, entire output = " + entireOutputStr << endl;
                
                //cout << "substr = " + subStr << endl;
                
                for(int i=0; i<iterationsNum; i++)
                {
                    output += subStr;
                }
                
                digitPreviouslySeen = false;
                
                //should only save output if not within another pair of brackets 
                if(withinBrackets <= 0)
                {
                    entireOutputStr = output + entireOutputStr;
                }
                    
                //cout << "after, entire output = " + entireOutputStr << endl;
                
                substrEndIndex = sPtr;
            }
            
            //establish start substr pntr
            if(s[sPtr] == '[') //char != str in c++
            {
                substrStartIndex = sPtr + 1;
                
                iterationsStr = "";
                
                withinBrackets--;
            }
            //establish end substr pntr
            else if(s[sPtr] == ']')
            {
                substrEndIndex = sPtr - 1;
                
                output = "";
                
                withinBrackets += 1;
            }
            //if char not tween brackets
            else if(withinBrackets <= 0 and !isDigit)
            {
                entireOutputStr = s[sPtr] + entireOutputStr;
            }
        }
        
        return entireOutputStr;
    }
};