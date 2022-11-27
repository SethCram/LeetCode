#include "FirstBadVersion.h" 
#include <stdio.h>

int main()
{
    Solution solution = Solution();

    int badVersion = solution.firstBadVersion(2126753390);

    printf("First bad version is %d", badVersion);
}