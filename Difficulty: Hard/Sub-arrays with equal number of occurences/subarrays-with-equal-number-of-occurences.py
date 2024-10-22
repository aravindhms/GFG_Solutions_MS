#User function Template for python3
from collections import defaultdict
class Solution:
    def sameOccurrence(self, arr, x, y):
        diff_map = defaultdict(int)
        
        # Initialize diff to 0 (no difference at the start)
        diff_map[0] = 1  # To handle subarrays starting from index 0
        diff = 0
        count = 0
        
        # Traverse the array
        for num in arr:
            if num == x:
                diff += 1
            elif num == y:
                diff -= 1
            
            # If the current diff has been seen before, it means we found
            # subarrays where counts of x and y are equal.
            count += diff_map[diff]
            
            # Increment the occurrence of the current diff
            diff_map[diff] += 1
        
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        y = int(input().strip())
        ob = Solution()
        ans = ob.sameOccurrence(arr, x, y)
        print(ans)
        tc -= 1

# } Driver Code Ends