from collections import defaultdict

class Solution:
    """
    You are given an array of strings words. Each element of words consists of two lowercase English letters.

    Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

    Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

    A palindrome is a string that reads the same forward and backward.
    """
    def longestPalindrome(self, words: list[str]) -> int:
        """Uses recursion to create all possible word combos, 
        those who are the same reversed are palindromes.

        Args:
            words (list[str]): _description_

        Returns:
            int: _description_
        """
        
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
            
    
    def longestPalindrome_sol(self, words: list[str]) -> int:
        """Number of paired words/letters = length of longest palindrome
        
        Don't actualy need to create longest palindrome, just need to find longest one's length.
        
        Counting Mirror Words O(n)
        
        2 letter words can be of 2 types:

        Where both letters are same
        Where both letters are different
        Based on the above information:

        If we are able to find the mirror of a word, ans += 4
        The variable unpaired is used to store the number of unpaired words with both letters same.
        Unpaired here means a word that has not found its mirror word.
        At the end if unpaired same letter words are > 0, we can use one of them as the center of the palindromic string.

        Args:
            words (list[str]): _description_

        Returns:
            int: _description_
        """
        
        mirroredWords = defaultdict(int) #if key not found, it's added with its value as one or whatever is assigned to it

        unpaired = 0
        answr = 0
        
        for twoLetterWord in words:
            #if letters are the same
            if twoLetterWord[0] == twoLetterWord[1]:
                #found a pair 
                
                #if atleast 1 matching word w/ same letters already in dict 
                if mirroredWords[twoLetterWord] > 0:
                    #found the mirror of the word
                    unpaired -= 1
                    mirroredWords[twoLetterWord] -= 1
                    answr += 4 # adds 4 bc everytime a pair is found, 4 chars are added to answer of longest palindrome
                #if matching word not in dict
                else:
                    #account for pair added to dict
                    mirroredWords[twoLetterWord] += 1
                    unpaired += 1 #incr unpaired just in case its mirror not found (can still use as center)
            #if letters aren't the same
            else:
                #if reversed word in dict
                if mirroredWords[twoLetterWord[::-1]] > 0:
                    #found mirror of word
                    answr += 4
                    mirroredWords[twoLetterWord[::-1]] -= 1
                    
                #if reverse of word not in dict
                else:
                    #incr count to try and find its mirror
                    mirroredWords[twoLetterWord] += 1
                    
        #if any number of unpaired words leftover
        if unpaired > 0:
            #incr palindrom count by 2 since placed in middle of palindrome 
            # and unpaired word of same letters (only even number of letters in a palindrome)
            answr += 2
        
        return answr
                    

            
sol = Solution()

rslt = sol.longestPalindrome_sol(words= ["ab","ty","yt","lc","cl","ab"]) #["lc","cl","gg"])

print( f"Longest palindrome's length = {rslt}")