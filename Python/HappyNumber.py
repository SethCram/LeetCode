from math import floor

class Solution:
    """
    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:

        Starting with any positive integer, replace the number by the sum of the squares of its digits.
        Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
        Those numbers for which this process ends in 1 are happy.

    Return true if n is a happy number, and false if not.
    """
    def isHappy(self, n: int) -> bool:
        """Hashmap approach using int-string conversion
        Speed: O(I^D) where I = number of itermediary numbers, D = average number of digits in a number
        Space: O(I) 

        Args:
            n (int): _description_

        Returns:
            bool: _description_
        """

        hashMap = dict()

        #maxIterations = 20
        #iterationCounter = 0

        while n != 1:
            #iterationCounter += 1

            #if iterationCounter >= maxIterations:
            #    return False

            print(n)

            nStr = str(n)

            n = sum( int(digitStr)**2 for digitStr in nStr )

            #if loop found
            if n in hashMap:
                return False
            else:
                hashMap[n] = 0

        return True

class Solution2:
    def isHappy(self, n: int) -> bool:
        """Hashmap approach using entirely integers
        Speed: O(I^D) where I = number of itermediary numbers, D = average number of digits in a number
        Space: O(I) 

        Args:
            n (int): _description_

        Returns:
            bool: _description_
        """

        hashMap = dict()

        #maxIterations = 20
        #iterationCounter = 0

        while n != 1:
            #iterationCounter += 1

            #if iterationCounter >= maxIterations:
            #    return False

            #print(n)

            summation = 0

            while n >= 1:

                #get the ones places digit
                onesPlaceDigit = n % 10

                #print(onesPlaceDigit)

                #sum square of digit
                summation += onesPlaceDigit**2

                #shift digits right
                n = floor(n / 10)

            n = summation 

            #if loop found
            if n in hashMap:
                return False
            else:
                hashMap[n] = 0

        return True
    
class Solution3:

    def advanceNumber(self, n: int) -> int:
        summation = 0
       
        while n >= 1:

            #get the ones places digit
            onesPlaceDigit = n % 10

            #sum square of digit
            summation += onesPlaceDigit**2

            #shift digits right
            n = floor(n / 10)
        
        return summation 

    def isHappy(self, n: int) -> bool:
        """Tortoise and Hare/Floyd Cycle Detection alg (double pointer approach) with just ints
        Speed: O(I^D) where I = number of itermediary numbers, D = average number of digits in a number
        Space: O(1)

        Args:
            n (int): _description_

        Returns:
            bool: _description_
        """

        slow = n
        fast = n

        while True:
            
            slow = self.advanceNumber(slow)
            fast = self.advanceNumber(fast)
            fast = self.advanceNumber(fast)
            if slow == fast:
                break
        
        return slow == 1