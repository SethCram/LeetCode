class Solution:
    """
    You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

    Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

        A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
        A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.

    We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

    Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.
    """
    def findBall(self, grid: list[list[int]]) -> list[int]:
        """Iterative solution using adjacent tiles
        Speed: O(N) since only iterate over each cell once,
            but do look at some cells more than once
        Space: O(1) bc only spaced used needed for output

        Args:
            grid (list[list[int]]): _description_

        Returns:
            list[int]: _description_
        """
        
        M = len(grid)
        N = len(grid[0])

        balls = []
        
        for i in range(M):

            for j in range(N):
                #if on first row, create list of balls from their starts
                if i == 0:
                    balls.append(j)
                
                #cache arr acces incase of mult uses
                
                #cache curr ball position
                currBall = balls[j]
                #cache curr ball position's grid cell val
                currGridCell = grid[i][currBall]
                
                #if ball not already stuck
                if currBall != -1:
                    #if right slant
                    if currGridCell == 1:
                        #if leads into wall or V, ball stuck
                        if currBall == N-1 or grid[i][currBall+1] == -1:
                            balls[j] = -1
                        #if opening
                        else:
                            #ball moves right
                            balls[j] += 1 
                    #if left slant
                    else:
                        #if leads into wall or V, ball stuck
                        if currBall == 0 or grid[i][currBall-1] == 1:
                            balls[j] = -1
                        #if opening
                        else:
                            #ball moves left
                            balls[j] -= 1 

            print(balls)
            
        return balls