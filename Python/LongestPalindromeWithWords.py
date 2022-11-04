class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        
        comboStrs = words[:]
        
        print(words[0])
        
        words2D  = [[twoLetterWord] for twoLetterWord in words]
        
        self.CreateAllStrs(words2D, words2D, comboStrs)  
        
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
                if "".join(twoLetterWord) not in currWord: #doesn't work bc doesn't account for duplicate 2 letter word in words
                    nextWordsList.append( currWord + twoLetterWord )
                    
                    comboStrs.append( "".join(nextWordsList[-1]) )
             
        if nextWordsList == []:
            raise ValueError
                    
        #comboStrs.append(nextWordsList[:])
        
        self.CreateAllStrs(nextWordsList, twoLetterWords, comboStrs)
            
sol = Solution()

rslt = sol.longestPalindrome(words=["ab","ty","yt","lc","cl","ab"]) #["lc","cl","gg"])

print( f"Longest palindrome's length = {rslt}")