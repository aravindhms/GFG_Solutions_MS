#User function Template for python3

class Solution:

    def findMinDiff(self, arr,m):

        # code here
        n = len(arr)
        if m == 0 or n == 0:
            return 0
        arr.sort()
        if n < m:
            return -1
        min_diff = float('inf')
        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            if diff < min_diff:
                min_diff = diff
        return min_diff