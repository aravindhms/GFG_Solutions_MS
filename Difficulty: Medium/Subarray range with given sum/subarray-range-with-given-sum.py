#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}

        for num in arr:
            prefix_sum += num
            if prefix_sum - tar in prefix_map:
                count += prefix_map[prefix_sum - tar]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return count

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends