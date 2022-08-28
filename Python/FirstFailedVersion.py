from importlib.metadata import version


class Solution:
    """
    You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the followIndexing ones to be bad.

    You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
    """
    def isBadVersion(self, versionNumber: int ) -> bool:
        return versionNumber >= 10
    
    def firstBadVersion(self, n: int) -> int:
        highIndex = n
        lowIndex = 0
        
        #Dictionaries are used to store data values in key:value pairs. (dont actually need dictionary)
        testedNumbers = {
          -1: False #false = good version
        }
        
        #while both search indices haven't converged 
        while( lowIndex != highIndex):
            #find new middle index
            midIndex = int( (highIndex + lowIndex) / 2 )
            
            print("new mid index = ", midIndex)
            print("high index = ", highIndex)
            print("low index = ", lowIndex)
            
            isMiddleBadVersion = midIndex >= 5
            
            #add to dictionary whether this version number is bad
            testedNumbers[midIndex] = isMiddleBadVersion
            
            #if point tween high+low is bad
            if( isMiddleBadVersion ):
                
                #find if version right before is bad
                versionBeforeIsBad = testedNumbers.get(midIndex-1) #get rets None of no key of that val in dictionary
                
                #if version before's been tested and it's good
                if(versionBeforeIsBad != None and versionBeforeIsBad == False): 
                    #return the mid index version as the first bad version
                    return midIndex
              
                #assign new high index at discovered bad version
                highIndex = midIndex 
            #if point tween high + low isnt bad
            else:
                #assign new bot index right above good version
                lowIndex = midIndex + 1
            
        #return one of the converged indices
        return highIndex

print( Solution.firstBadVersion(self=Solution, n=10) )