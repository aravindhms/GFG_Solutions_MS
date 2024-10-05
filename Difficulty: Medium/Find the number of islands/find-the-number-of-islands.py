#User function Template for python3
from collections import deque
class Solution:
    def numIslands(self, grid):
        # code here
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            
            while queue:
                x, y = queue.popleft()
                for di, dj in directions:
                    new_x, new_y = x + di, y + dj
                    if 0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y] and grid[new_x][new_y] == 1:
                        visited[new_x][new_y] = True
                        queue.append((new_x, new_y))

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    bfs(i, j)
                    count += 1
        return count


#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.numIslands(grid))

# } Driver Code Ends