#include <vector>

/// @brief There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time. Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner. The test cases are generated so that the answer will be less than or equal to 2 * 109.
class Solution {
public:
    /// @brief we have the base cases dp[0][j] = dp[i][0] = 1 for all valid i and j
    /// @brief O(m * n) time and costs O(n) space
    /// @param m 
    /// @param n 
    /// @return 
    int uniquePaths(int m, int n) {
        //init vect with all 1s and size of n
        std::vector<int> cur(n, 1);
        //walk thru all rows starting at 1st instead of 0th (no cells above 0th row )
        for (int i = 1; i < m; i++) {
            //walk thru all cols starting at 1st instead of 0th (no cells left of 0th col)
            for (int j = 1; j < n; j++) {
                //accumulate all cells 
                cur[j] += cur[j - 1];
            }
        }
        return cur[n - 1];
    }
};