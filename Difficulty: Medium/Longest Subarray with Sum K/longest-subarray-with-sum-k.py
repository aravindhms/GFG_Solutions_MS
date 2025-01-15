# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        prefix_sum = 0
        max_length = 0
        prefix_map = {}

        for i, num in enumerate(arr):
            prefix_sum += num

            if prefix_sum == k:
                max_length = max(max_length, i + 1)

            if prefix_sum - k in prefix_map:
                max_length = max(max_length, i - prefix_map[prefix_sum - k])

            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i

        return max_length
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends