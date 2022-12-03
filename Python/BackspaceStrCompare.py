class Solution:
    """
    Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

    Note that after backspacing an empty text, the text will continue empty.
    """
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Speed: O(S+T) where S = number of chars in s, T = number of chars in T
        Space: O(1) bc only counters, temp vars, and pointers used

        Args:
            s (str): _description_
            t (str): _description_

        Returns:
            bool: _description_
        """
        
        sBackspaces = 0
        tBackspaces = 0
        
        sLen = len(s)
        tLen = len(t)
        
        #start both pntrs at end of their words
        sPtr = sLen - 1
        tPtr = tLen - 1
        
        while tPtr >= 0 or sPtr >= 0:
            
            #walk thru part of s
            while sPtr >= 0:
                #if # found
                if s[sPtr] == "#":
                    #add to # counter
                    sBackspaces += 1
                    #advance to next char
                    sPtr -= 1  
                #if backspaces left
                elif sBackspaces > 0:
                    #rm from # counter
                    sBackspaces -= 1
                    #advance to next char
                    sPtr -= 1  
                #no # found and no backspaces left
                else:
                    #stop looping
                    break
                
            #walk thru part of t
            while tPtr >= 0:
                #if # found
                if t[tPtr] == "#":
                    #add to # counter
                    tBackspaces += 1
                    #advance to next char
                    tPtr -= 1  
                #if backspaces left
                elif tBackspaces > 0:
                    #rm from # counter
                    tBackspaces -= 1
                    #advance to next char
                    tPtr -= 1  
                #no # found and no backspaces left
                else:
                    #stop looping
                    break
            
            #if letters unequal, or letters left in one word but not the other
            if( (sPtr >= 0 and tPtr >= 0 and s[sPtr] != t[tPtr]) or 
                (sPtr >= 0 and tPtr < 0) or 
                (tPtr >= 0 and sPtr < 0)):
                return False
            else:
                #letters r same so comp next pair
                sPtr -= 1
                tPtr -= 1
        
            
        
        return True
            