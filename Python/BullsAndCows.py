from collections import defaultdict

class Solution:
    """
    You are playing the Bulls and Cows game with your friend.

    You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

        The number of "bulls", which are digits in the guess that are in the correct position.
        The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.

    Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

    The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.
    """
    def getHint(self, secret: str, guess: str) -> str:
        """Double number count dict/hashmap approach
        Speed: O(N)
        Space: O(1), at worst it's O(20) since 10 possible digits and 2 hashmaps used

        Args:
            secret (str): _description_
            guess (str): _description_

        Returns:
            str: _description_
        """
        
        secretUnequalCountDict = defaultdict(int)
        
        guessUnequalCountDict = defaultdict(int)
        
        cows = 0
        
        bulls = 0
        
        for i in range(len(secret)):
            
            secretDigit = secret[i]
            guessDigit = guess[i]
            
            if secretDigit == guessDigit:
                bulls += 1
            else:
                
                #if a useable digit found in the other number's history
                if guessUnequalCountDict[secretDigit] > 0:
                    #found a correct digit but in wrong pos
                    cows += 1
                    #use up digit
                    guessUnequalCountDict[secretDigit] -= 1
                else:
                    #remember digit as unpaired
                    secretUnequalCountDict[secretDigit] += 1
                    
                #if a useable digit found in the other number's history
                if secretUnequalCountDict[guessDigit] > 0:
                    #found a correct digit but in wrong pos
                    cows += 1
                    #use up digit
                    secretUnequalCountDict[guessDigit] -= 1
                    
                else:
                    #remember digit as unpaired
                    guessUnequalCountDict[guessDigit] += 1
                    
            
        
        return f"{bulls}A{cows}B"