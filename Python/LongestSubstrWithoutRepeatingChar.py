class Solution:
    """
        Given a string s, find the length of the longest substring without repeating characters.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Sliding window/double pointer technique with default dictionary.
        Speed: O(N)
        Space: O(M), M = number of unique characters in s

        Args:
            s (str): _description_

        Returns:
            int: _description_
        """
        
        prevChars = dict() #could potentially use set so not as much space taken by repeating chars
        
        #if val not found, establish it in dict as val of None
        prevChars.setdefault(None)
        
        ptr1 = 0
        
        longestSubtrLen = 0
        
        strLen = len(s)
        
        #walk thru str elly by elly
        for ptr2, char in enumerate(s):
            
            prevCharIndex = prevChars.get(char)
            
            #if char already seen in substr and within range of sliding window
            if prevCharIndex != None and prevCharIndex >= ptr1:
                currSubstrLen = ptr2 - ptr1
                
                #if curr substr len is the longest
                if currSubstrLen > longestSubtrLen:
                    longestSubtrLen = currSubstrLen
                
                #move ptr1 to start of nxt substr as right in front of previously repeated char
                ptr1 = prevCharIndex + 1
                
            else:
                #if last char
                if ptr2 + 1 == strLen:
                    
                    currSubstrLen = ptr2 - ptr1 + 1
                    
                    #if curr substr len is the longest
                    if currSubstrLen > longestSubtrLen:
                        longestSubtrLen = currSubstrLen    
            
            #add char to dict with index found at
            prevChars[char] = ptr2
                
        return longestSubtrLen
                
                
sol = Solution()
print( sol.lengthOfLongestSubstring("pwwkew") )
print( sol.lengthOfLongestSubstring("dvdf") )
