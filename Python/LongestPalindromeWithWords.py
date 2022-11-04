class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        
        comboStrs = words[:]
        
        words2D  = [[twoLetterWord] for twoLetterWord in words]
        
        self.CreateAllStrs(words2D, words, words2D, comboStrs)  
        
        #walk thru combo strs
        for i in range(1, len(comboStrs)+1):
            #walk backwards since sorted in ascending size order
            comboStr = comboStrs[-i]
            
            reversedComboStr = comboStr[::-1] #comboStr[len(comboStr):0] #reversed(comboStr) 
            
            if comboStr == reversedComboStr:
                
                print(f"Longest palindrome is {comboStr}")
                
                return len(comboStr)
        
        return 0
    
    def CreateAllStrs(self, currWordList, twoLetterWords, twoLetterWordsList, comboStrs):
        
        if len(currWordList[-1]) == len(twoLetterWords):
            return
        
        nextWordsList = []

        for currWord in currWordList:
            for i in range(len(twoLetterWords)):
                
                #if "".join(twoLetterWord) not in currWord: #doesn't work bc doesn't account for duplicate 2 letter word in words
                if currWord.count(twoLetterWords[i]) != twoLetterWords.count(twoLetterWords[i]): #if haven't reached num of duplicated within currWord
                    nextWordsList.append( currWord + twoLetterWordsList[i] )
                    
                    comboStrs.append( "".join(nextWordsList[-1]) )
             
        if nextWordsList == []:
            raise ValueError
                    
        #comboStrs.append(nextWordsList[:])
        
        self.CreateAllStrs(nextWordsList, twoLetterWords, twoLetterWordsList, comboStrs)
            
sol = Solution()

rslt = sol.longestPalindrome(words= ["ab","ty","yt","lc","cl","ab"]) #["lc","cl","gg"])

print( f"Longest palindrome's length = {rslt}")