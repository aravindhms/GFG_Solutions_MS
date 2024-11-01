#User function Template for python3

class Solution:
    def maxSum(self,arr):
		arr.sort()
		
		# Create two pointers: one at the beginning and one at the end
		n = len(arr)
		left, right = 0, n - 1
		
		# Rearrange the elements in an alternating order
		result = []
		while left < right:
			result.append(arr[right])
			result.append(arr[left])
			right -= 1
			left += 1
		
		if left == right:
			result.append(arr[left])
		
		# Calculate the maximum sum of absolute differences
		max_sum = 0
		for i in range(n):
			max_sum += abs(result[i] - result[(i + 1) % n])
		
		return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends