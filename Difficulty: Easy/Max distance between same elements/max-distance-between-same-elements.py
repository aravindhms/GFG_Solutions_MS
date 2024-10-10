class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        element_indices = {}
        max_dist = 0

        for i in range(len(arr)):
            if arr[i] in element_indices:
                max_dist = max(max_dist, i - element_indices[arr[i]])
            else:
                element_indices[arr[i]] = i

        return max_dist


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends