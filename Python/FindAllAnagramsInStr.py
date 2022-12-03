from collections import defaultdict

class Solution:
    """
    Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    """
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """Sliding window 
        Speed: O(P + S) bc iterate once thru s and once thru p, 
            worst case O(P + 26*S) bc everytime go thru S, iterate thru entire hashmap
        Space: O(1) bc hashmap uses constant space,
            worst would be O(26)

        Args:
            s (str): _description_
            p (str): _description_

        Returns:
            list[int]: _description_
        """
        
        #populate p count dict
        pCountDict = defaultdict(int)
        for pElly in p:
            pCountDict[pElly] += 1
        
        substrIndices = []
        
        pLen = len(p)
        
        #window start
        j = 0
        
        #walk thru chars in s
        for i,sElly in enumerate(s):
            
            #move top of window
            if sElly in pCountDict: 
                #rm one occurence of s char from p
                pCountDict[sElly] -= 1
                
            #if window been established
            if i >= pLen:

                #if number leaving bot of window was kept track of
                if s[j] in pCountDict:
                    #readd one occurence of s char from p
                    pCountDict[s[j]] += 1
                #advance bot of window
                j += 1
            
            #if no chars left to use, anagram found
            if all(occurences == 0 for occurences in pCountDict.values()):
                #append starting index of substr
                substrIndices.append(j)
        
        return substrIndices