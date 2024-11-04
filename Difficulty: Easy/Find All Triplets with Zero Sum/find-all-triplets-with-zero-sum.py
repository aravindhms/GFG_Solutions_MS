#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        from collections import defaultdict
        n = len(arr)
        def collect(i):
            target, m = -arr[i], defaultdict(list)
            for j in range(i+1, n):
                if target - arr[j] in m:
                    for idx in m[target-arr[j]]:
                        yield i, idx, j
                m[arr[j]].append(j)
        for i in range(n):
            yield from collect(i)

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        ob = Solution()
        res = ob.findTriplets(A)
        res = sorted(res)
        if len(res) == 0:
            print('[]')
        for i in range(len(res)):
            for j in range(len(res[i])):
                print(res[i][j], end=" ")
            print("")
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends