from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        """Doesn't work

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

        #window start
        j = 0
        
        #walk thru chars in s
        for i,sElly in enumerate(s):
            #if s char is in p and can still use that char
            if sElly in pCountDict and pCountDict[sElly] > 0:
                #rm one occurence of s char from p
                pCountDict[sElly] -= 1
                
                #if no chars left to use, anagram found
                if all(occurences == 0 for occurences in pCountDict.values()): #(i - j) + 1 == pLen: 
                    #append starting index of substr
                    substrIndices.append(j)
                    
                    if s[j] in pCountDict:
                        #readd one occurence of s char from p
                        pCountDict[s[j]] += 1
                    
                    #advance bot of window
                    j += 1
                
                #print(pCountDict)
            else:
                #print(pCountDict)
                if s[j] in pCountDict:
                    #readd one occurence of s char from p
                    pCountDict[s[j]] += 1
                #print(pCountDict)
                
                #advance bot of window
                j += 1
        
        return substrIndices
            