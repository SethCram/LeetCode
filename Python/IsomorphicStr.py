from collections import defaultdict

class Solution:
    """
    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        tCount = defaultdict(int)
        sCount = defaultdict(int)
        
        for i in range(len(t)):
            tCount[t[i]] += 1
            sCount[s[i]] += 1
            
            if tCount[t[i]] != sCount[s[i]]:
                return False
            
        return True
            
sol = Solution()
print(sol.isIsomorphic("egg", "add"))