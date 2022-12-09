class Solution:
    """
        Given an m x n matrix, return all elements of the matrix in spiral order.
    """
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        """iterative approach of repeatedly going right, down, left, up
        Speed: O(N)
        Space: O(N) for visited list,
            could decrease to O(1) thru incring/decring colCount and rowCount 
            instead of using visited array

        Args:
            matrix (list[list[int]]): _description_

        Returns:
            list[int]: _description_
        """

        M = len(matrix)
        N = len(matrix[0])

        visited = [ [False]*N for row in matrix]
        #print(visited)

        #init coords and spiral list w/ starting node
        x = 0
        y = 0
        spiralOrderList = [matrix[y][x]]
        visited[x][y] = True

        #while can still continue cycle and move to the right or down
        while( 
            x + 1 < N and not visited[y][x+1] or
            y + 1 < M and not visited[y+1][x]
        ):
            
            #walk to end of right path
            rightX = x + 1
            while rightX < N and not visited[y][rightX]:
                x = rightX
                visited[y][x] = True
                spiralOrderList.append(matrix[y][x])
                rightX = x + 1
            
            #walk to end of down path
            downY = y + 1
            while downY < M and not visited[downY][x]:
                y = downY
                visited[y][x] = True
                spiralOrderList.append(matrix[y][x])
                downY = y + 1
            
            #walk to end of left path
            leftX = x - 1
            while 0 <= leftX and not visited[y][leftX]:
                x = leftX
                visited[y][x] = True
                spiralOrderList.append(matrix[y][x])
                leftX = x - 1
            
            #walk to end of up path
            upY = y - 1
            while 0 <= upY and not visited[upY][x]: #dont have to check for 0 here
                y = upY
                visited[y][x] = True
                spiralOrderList.append(matrix[y][x])
                upY = y - 1
        
        return spiralOrderList
            
        