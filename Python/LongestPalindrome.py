from collections import defaultdict

class Solution:
    """
    Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

    Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
    """
    def longestPalindrome(self, s: str) -> int:
        """Dictionary approach
        Speed: O(N)
        Space: O(M) where M = number of unique chars

        Args:
            s (str): _description_

        Returns:
            int: _description_
        """
        charCount = defaultdict(int)
        
        unpaired = 0
        paired = 0
        
        #walk thru every char in str
        for c in s:
            #incr char count since seen
            charCount[c] += 1
            
            #even time char seen
            if charCount[c] % 2 == 0:
                paired += 2
                unpaired -= 1
            #odd time char seen
            else:
                unpaired += 1
        #any unpaired chars
        if unpaired > 0:
            #only use one unpaired char
            return paired + 1
        #no unpaired chars
        else:
            return paired
                