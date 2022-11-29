/** You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    Speed: O(N-2) bc first 2 steps initialized as (still O(N) technically)
    Space: O(1)
 * @param {number} n desired stair
 * @return {number} distinct climbs to reach desired stair
 */
 var climbStairs = function(n) {
    //init vars
    prevPrevNum = 1;
    prevNum = 2;
    
    //if not bigger than base cases, return as them
    if(n == prevNum) return prevNum;
    if(n == prevPrevNum) return prevPrevNum;
    
    //accumulate distinct climbs per num of stairs till reach desired stair
    for(i = 3; i <= n; i++)
    {
        currNum = prevNum + prevPrevNum;
        prevPrevNum = prevNum;
        prevNum = currNum;
    }
    
    //return distinct climbs to reach desired stair
    return prevNum;
};