# your task is to complete this function
# function should return index to the any valid peak element
class Solution:   
    def peakElement(self,arr, n):
		n = len(arr)
		low, high = 0, n - 1
		
		while low <= high:
			mid = (low + high) // 2
			
			# Check if mid is a peak
			if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == n - 1 or arr[mid] >= arr[mid + 1]):
				return mid
			
			# If the left neighbor is greater, move left
			if mid > 0 and arr[mid - 1] > arr[mid]:
				high = mid - 1
			else:
				low = mid + 1
		
		return -1        # Code here



#{ 
 # Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends