#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

# from typing import List
from collections import deque


class Solution:
    def rotateDelete(self,  arr):
        # code here
        ind=0
        ind_2=0
        ind_3=len(arr)-1
        while(len(arr)!=1):
            x = arr[len(arr)-1]
            arr.insert(0,x)
            arr.pop(len(arr)-1)
            y = ind_3-ind-ind_2
            y = 0 if y<0 else y
            arr.pop(y)
            ind+=1
            ind_2+=1
        return arr[0]


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.rotateDelete(arr)
        print(res)
        t -= 1


# } Driver Code Ends