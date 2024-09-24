import heapq
class Solution:
    
    #Function to return the minimum cost to react at bottom
	#right cell from top left cell.
	def minimumCostPath(self, grid):
		N = len(grid)
		directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
		cost = [[float('inf')] * N for _ in range(N)]
		cost[0][0] = grid[0][0]
		
		pq = [(grid[0][0], 0, 0)]
		
		while pq:
			current_cost, x, y = heapq.heappop(pq)
			
			if x == N-1 and y == N-1:
				return current_cost
			
			for dx, dy in directions:
				nx, ny = x + dx, y + dy
				if 0 <= nx < N and 0 <= ny < N:
					new_cost = current_cost + grid[nx][ny]
					if new_cost < cost[nx][ny]:
						cost[nx][ny] = new_cost
						heapq.heappush(pq, (new_cost, nx, ny))
		
		return -1


#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	grid = []
	for _ in range(n):
		a = list(map(int, input().split()))
		grid.append(a)
	obj = Solution()
	ans = obj.minimumCostPath(grid)
	print(ans)

# } Driver Code Ends