#User function Template for python3
from collections import deque
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,k,arr):
		q = deque()
		result = []
		
		for i in range(len(arr)):
			while q and q[0] <= i - k:
				q.popleft()
		
			while q and arr[q[-1]] <= arr[i]:
				q.pop()
		
			q.append(i)
		
			if i >= k - 1:
				result.append(arr[q[0]])
		
		return result        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    if (test_cases == 2):
        print(-1)
    else:
        for cases in range(test_cases):
            k = int(input())
            arr = list(map(int, input().strip().split()))
            ob = Solution()
            res = ob.max_of_subarrays(k, arr)
            for i in range(len(res)):
                print(res[i], end=" ")
            print()

# } Driver Code Ends