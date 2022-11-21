from collections import defaultdict

class Solution:
    """
    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        """Tracks each chars last known index and count of each char
        Speed: O(N)
        Space: O(M^2 * P^2) where M = number of unique chars in s, 
            P = number of unique chars in t

        Args:
            s (str): _description_
            t (str): _description_

        Returns:
            bool: _description_
        """
        #init dicts for each str to track occurences 
        # and indices of last seen occurence of char
        tCount = defaultdict(int) #inits unseen keys to 0 val
        tLastIndex = dict()
        sCount = defaultdict(int)
        sLastIndex = dict()
        
        for i in range(len(t)):
            #cache str chars 
            tElly = t[i]
            sElly = s[i]
            
            #calc new occurence count
            newTCount = tCount[tElly] + 1
            newSCount = sCount[sElly] + 1
            #set new occurence count
            tCount[tElly] = newTCount
            sCount[sElly] = newSCount
            
            #if new counts aren't equal 
            if newTCount != newSCount:
                return False
            #if new counts are equal but last seen indices are diff
            elif newTCount > 1 and tLastIndex[tElly] != sLastIndex[sElly]:
                return False
            
            #store last seen index of curr elly
            tLastIndex[tElly] = i
            sLastIndex[sElly] = i
            
        return True
            
sol = Solution()
print(sol.isIsomorphic("egg", "add"))