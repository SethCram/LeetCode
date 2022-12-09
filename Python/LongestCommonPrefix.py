class Solution:
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".
    """
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """Vertical character comparison
        Speed: O(N), scales linearly with shortest common substr/word
        Space: O(1), could cache word length in additional data structurefor additional speed
        
        Could potentially transpose matrix instead and loop in a normal fashion instead of vertically

        Args:
            strs (list[str]): _description_

        Returns:
            str: _description_
        """

        strsLen = len(strs)

        if strsLen == 1:
            return strs[0]

        prefix = ""

        #walk thru chars of 1st word
        for i in range(len(strs[0])):
            
            currLetter = strs[0][i]

            #walk thru all other words
            for j in range(1, strsLen): #assumes atleast 2 strs 

                currWord = strs[j]

                withinBounds = (i < len(currWord)) 

                #if still within bounds for curr word
                if withinBounds:
                    #store whether same letter
                    sameLetter = (currWord[i] == currLetter)

                    if not sameLetter:
                        break
                else:
                    break
            
            #if found letter that's not the same or outside of bounds for a word
            if not withinBounds or not sameLetter:
                break
            #letters are all the same, so add to running word
            else:
                prefix += currLetter
        
        return prefix


        