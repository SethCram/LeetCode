from copy import deepcopy
#import numpy as np

class Solution:
    """
    An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

    You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

    To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

    Return the modified image after performing the flood fill.
    """
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        """DFS preOrder traversal
        Speed: O(V + E) where V = number of vertice and E = number of edges
        Space: O(V^2)
        Auxilliary Space: O(V) since a list of visited vertices is tracked 

        Args:
            image (list[list[int]]): _description_
            sr (int): _description_
            sc (int): _description_
            color (int): _description_

        Returns:
            list[list[int]]: _description_
        """
        #store m x n image coords
        m = len(image)
        n = len(image[0])
        
        visited = [ [False]*n for _ in range(m)] #[[False]*n]*m  #np.empty( (m, n), dtype=bool) #time to fill this arr not accounted for
        
        #print(f"{image}, {visited}")
        
        rootColor = image[sr][sc]
        
        if rootColor == color:
            return image
        
        #need to copy for list or else just assigned a ref
        newImage = deepcopy(image)
        
        return self.floodFill_HeavyLifting(m, n, newImage, visited, sr, sc, rootColor, color)
        
    
    def floodFill_HeavyLifting(self, m, n, newImage, visited, x, y, rootColor, newColor):
        
        #assign new color
        newImage[x][y] = newColor
        #mark as visited
        visited[x][y] = True
        
        #print(f"{newImage}, {visited}")
        
        #if pixel connected 4-directionally + root colored + not yet visited, call funct again with new coords
        newX = x - 1
        if newX >= 0 and newImage[newX][y] == rootColor and not visited[newX][y]:
            newImage = self.floodFill_HeavyLifting( m, n, newImage, visited, newX, y, rootColor, newColor)
        
        newX = x + 1
        if newX < m and newImage[newX][y] == rootColor and not visited[newX][y]:
            newImage = self.floodFill_HeavyLifting( m, n, newImage, visited, newX, y, rootColor, newColor)
        
        newY = y - 1
        if newY >= 0 and newImage[x][newY] == rootColor and not visited[x][newY]:
            newImage = self.floodFill_HeavyLifting( m, n, newImage, visited, x, newY, rootColor, newColor)
        
        newY = y + 1
        if newY < n and newImage[x][newY] == rootColor and not visited[x][newY]:
            newImage = self.floodFill_HeavyLifting( m, n, newImage, visited, x, newY, rootColor, newColor)
        
        return newImage
        