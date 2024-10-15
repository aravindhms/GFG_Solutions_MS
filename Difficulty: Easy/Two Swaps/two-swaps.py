class Solution:
    def checkSorted(self, arr):
        dist = {}
        for i in range(len(arr)):
            distance = arr[i] - (i + 1)
            if distance != 0:
                dist[i] = dist.get(i, 0) + distance
        pos = 0
        neg = 0
        for k, v in dist.items():
            if v > 0:
                pos +=1
            if v < 0:
                neg += 1
            if pos > 2 or neg > 2:
                return False
            if v*(-1) not in dist.values():
                return False
        return True
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends