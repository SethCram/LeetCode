from collections import defaultdict

class Solution:    
    """
    Given an array of strings words and an integer k, return the k most frequent strings.

    Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
    """
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        """Uses count dictionary, sorts array according to custom hashcode, iterates through sorted arr.
        Worst Speed: O(N^M) if M = average length of each word bc needa iterate thru it to get hashcode (or would it be just O(N)?)
        Space: O(N) for sorted array according to hashcode

        Args:
            words (list[str]): _description_
            k (int): _description_

        Returns:
            list[str]: _description_
        """
        
        #create word count dict
        wordsCountDict = defaultdict(int)
        for word in words:
            wordsCountDict[word] += 1
            
        #print(wordsCountDict)
        
        def hash_code(word):         
            #ASCII value of the lowercase alphabet is from 97 to 122      
            
            #99 bigger than 100 here
            asciiWord = "0." + "".join(str(ord(letter)) if ord(letter) >= 100 else "0" + str(ord(letter)) for letter in word)
            
            return wordsCountDict[word] - float(asciiWord)
        
        #print(words)
        #print([hash_code(word) for word in words])
        
        alphabeticWords = sorted(words, key=hash_code, reverse=True) #doesnt use sort() so words not clobbered
        
        sortedList = []
        
        for i in range(len(alphabeticWords)):
            if k == 0:
                break
                
            alphabeticWord = alphabeticWords[i]
            
            if alphabeticWord not in sortedList:
                sortedList.append(alphabeticWords[i])
                k -= 1
        
        return sortedList 