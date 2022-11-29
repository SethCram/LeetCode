class Solution:
    """
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
    """ 
    def numIslands(self, grid: list[list[str]]) -> int:
        """Uses recursion to visit all connected land cells when new island found.
        Worst Speed: O(N^2) about
        Best Speed: O(N)
        Space: O(N) bc don't wanna clobber input grid, otherwise could get O(1) by modifying grid itself to mark for visited

        Args:
            grid (list[list[str]]): _description_

        Returns:
            int: _description_
        """
        m = len(grid)
        n = len(grid[0])
        
        islands = 0
        
        visited = [ [False]*n for _ in range(m)]
        
        for i in range(m):
            
            for j in range(n):
                #if unvisited land tile
                if grid[i][j] == "1" and not visited[i][j]:
                    #mark all adjacent cells visited 
                    self.markIslandCellsVisited(grid, visited, i, j, m, n)
                    #count new island found
                    islands += 1
                
        return islands
    
    def markIslandCellsVisited(self, grid, visited, x, y, m, n) -> None:
        
        visited[x][y] = True
        
        newX = x - 1
        if newX >= 0 and grid[newX][y] == "1" and not visited[newX][y]:
            self.markIslandCellsVisited(grid, visited, newX, y, m, n)
        
        newX = x + 1
        if newX < m and grid[newX][y] == "1" and not visited[newX][y]:
            self.markIslandCellsVisited(grid, visited, newX, y, m, n)
            
        newY = y - 1
        if newY >= 0 and grid[x][newY] == "1" and not visited[x][newY]:
            self.markIslandCellsVisited(grid, visited, x, newY, m, n)
            
        newY = y + 1
        if newY < n and grid[x][newY] == "1" and not visited[x][newY]:
            self.markIslandCellsVisited(grid, visited, x, newY, m, n)
        
        return