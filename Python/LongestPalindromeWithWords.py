class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        
        comboStrs = words[:]
        
        self.CreateAllStrs(words, words, comboStrs)  
        
        #walk thru combo strs
        for i in range(1, len(comboStrs)+1):
            #walk backwards since sorted in ascending size order
            comboStr = comboStrs[-i]
            
            reversedComboStr = comboStr[::-1] #comboStr[len(comboStr):0] #reversed(comboStr) 
            
            if comboStr == reversedComboStr:
                
                print(f"Longest palindrome is {comboStr}")
                
                return len(comboStr)
        
        return 0
    
    def CreateAllStrs(self, currWordList, twoLetterWords, comboStrs):
        
        if len(currWordList[-1]) == len(twoLetterWords) * 2:
            return
        
        nextWordsList = []
        
        for currWord in currWordList:
            for twoLetterWord in twoLetterWords:
                if twoLetterWord not in currWord: #doesn't work bc doesn't segment word into pairs of 2 chars
                    nextWordsList.append( currWord + twoLetterWord )
                    
                    comboStrs.append( currWord + twoLetterWord )
                    
        #comboStrs.append(nextWordsList[:])
        
        self.CreateAllStrs(nextWordsList, twoLetterWords, comboStrs)
            
sol = Solution()

rslt = sol.longestPalindrome(words=["ab","ty","yt","lc","cl","ab"]) #["lc","cl","gg"])

print( f"Longest palindrome's length = {rslt}")