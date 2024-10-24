#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
		n = len(arr)
		# Step 1: Modify the array
		for i in range(n - 1):
			if arr[i] != 0 and arr[i] == arr[i + 1]:
				arr[i] *= 2
				arr[i + 1] = 0
		
		# Step 2: Rearrange the array
		result = [x for x in arr if x != 0]  # Collect all non-zero elements
		result.extend([0] * (n - len(result)))  # Append zeros at the end
		
		return result


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends