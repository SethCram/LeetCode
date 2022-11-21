class Solution:
    """
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        """Double pointer approach 
        Speed: O(N)
        Space: O(1)

        Args:
            s (str): _description_
            t (str): _description_

        Returns:
            bool: _description_
        """
        #if s is empty, its a subseq of t
        if s == "":
            return True 
        # if t is empty, s is not a subseq of t
        if t == "":
            return False
        
        tLen = len(t)
        sLen = len(s)
        
        sIndex = 0
        
        #walk thru t
        for tIndex in range(tLen):
            #if ellys same
            if s[sIndex] == t[tIndex]:
                #incr s index bc curr char found in t
                sIndex += 1
                
                #if found all of s
                if sIndex >= sLen:
                    #s found in t
                    return True
        
        return False
            