class Solution:
    def decodeString(self, s: str) -> str:
        
        iterationsStr = ""
        
        for i,sLetter in enumerate(s):
            
            if sLetter.isnumeric():
                iterationsStr += sLetter
            elif sLetter == '[':
                substrStartIndex = i + 1
                
            elif sLetter == ']':
                
                substrEndIndex = i - 1
                
                
                
                iterationsStr = ""