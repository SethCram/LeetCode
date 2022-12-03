from collections import defaultdict

class Solution:
    """
    You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

    Return the length of the longest substring containing the same letter you can get after performing the above operations.
    """
    def characterReplacement(self, s: str, k: int) -> int:
        """Uses sliding window with hashmap. Accepted solution but slowish.
        Worst Speed: O(26*26*S) where S is the number of characters in s,
            doesn't matter in long run so technically O(S)
        Worst Space: O(26) so a constant space of O(1)

        Args:
            s (str): _description_
            k (int): _description_

        Returns:
            int: _description_
        """
        #populate char count dict
        countDict = defaultdict(int)
        
        #window start
        j = 0
        
        longestLen = 0
        
        sLen = len(s)
        
        #walk thru chars in s
        for i,sElly in enumerate(s):
            
            #move top of window
            #add one occurence of s char
            countDict[sElly] += 1
                
            occurencesList = countDict.values()
                
            #if last char or too many repeating characters in window to replace
            if sum(occurencesList) - max(occurencesList) > k:
                
                windowLen = i - j #not plus one bc went 1 char too far
                
                if longestLen  < windowLen:
                    longestLen = windowLen
                
                #rm one occurence of s char at start of window
                countDict[s[j]] -= 1
                #advance bot of window
                j += 1
            elif i == sLen - 1:
                
                windowLen = i - j + 1 
                
                if longestLen  < windowLen:
                    longestLen = windowLen
                
                #rm one occurence of s char at start of window
                countDict[s[j]] -= 1
                #advance bot of window
                j += 1
        
        return longestLen
            
            