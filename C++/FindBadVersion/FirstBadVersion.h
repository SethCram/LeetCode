
/// @brief You are a product manager and currently leading a team to develop a new product. 
/// @brief Unfortunately, the latest version of your product fails the quality check. 
/// @brief Since each version is developed based on the previous version, all the versions after a bad version are also bad. 
/// @brief Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad. 
/// @brief You are given an API bool isBadVersion(version) which returns whether version is bad. 
/// @brief Implement a function to find the first bad version. You should minimize the number of calls to the API.
/// @brief The API isBadVersion is defined for you.
class Solution {
public:
    /// @brief atleast one version is bad
    /// @brief Speed: O(logN)
    /// @brief Space: O(1)
    /// @param n 
    /// @return 
    int firstBadVersion(int n) 
    {
        long int leftIndex = 0; //couldnt use regular int for some reason
        long int rightIndex = n - 1;

        long int middleIndex;
        long int middleNumber;

        bool isBad;

        while ( leftIndex <= rightIndex ) 
        {
            middleIndex = ((rightIndex + leftIndex) / 2); //implicit rounding to int
            middleNumber = middleIndex + 1;

            isBad = isBadVersion(middleNumber);

            if( isBad )
            {
                rightIndex = middleIndex - 1; //right index misses last bad version by 1
            }
            else
            {
                leftIndex = middleIndex + 1; //if indices are the same, left index advanced to first bad version
            }
        }

        return leftIndex + 1;
    }
private:
    bool isBadVersion(int version)
    {
        return version >= 1702766719;
    }
};