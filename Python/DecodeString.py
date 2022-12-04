from collections import deque

class Solution:
    """
    
    """
    def decodeString(self, s: str) -> str:
        """Stack approach to preserve ordering of substr and desired duplicate number.
        Speed: O(N)
        Space: O(N) bc scales linearly with larger s, but will likely never reach length of s
    
        Args:
            s (str): _description_

        Returns:
            str: _description_
        """
        stack = deque(); curNum = 0; curString = ''
        for c in s:
            #if start of new substring
            if c == '[':
                #add substring
                stack.append(curString)
                #add number of substrs desired
                stack.append(curNum)
                #reset to find next substr
                curString = ''
                #reset to find next num
                curNum = 0 
            #if end of new substring
            elif c == ']':
                #retrieve number and substr
                num = stack.pop()
                prevString = stack.pop()
                #create new str using previous str and duplicates of curr substr
                curString = prevString + num*curString
            #if digit
            elif c.isdigit():
                #moves pre-existing number left a digit and adds new number
                curNum = curNum*10 + int(c)
            #if char but not a bracket (must be a letter)
            else:
                curString += c
        return curString