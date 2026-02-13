class Solution:
    def getCount(self, n, d):
        # code here 
        low, high, res = 1, n, n + 1
        while low <= high:
            mid = (low + high) // 2
            val, temp = mid, mid
            s = 0
            while temp > 0:
                s += temp % 10
                temp //= 10
            if val - s >= d:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return max(0, n - res + 1)
