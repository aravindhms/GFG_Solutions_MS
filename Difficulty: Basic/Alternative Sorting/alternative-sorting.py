class Solution:
    def alternateSort(self,arr):
		# Sort the array
		arr.sort()
		
		# Create a new result array
		result = []
		
		# Pointers for the start (smallest) and end (largest) of the sorted array
		i, j = 0, len(arr) - 1
		
		# Alternate between the largest and smallest elements
		while i <= j:
			if i != j:
				result.append(arr[j])
				result.append(arr[i])
			else:
				result.append(arr[i])
			i += 1
			j -= 1
		
		return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends