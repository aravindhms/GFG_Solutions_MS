class Solution():
    def maxMinHeight(self, arr, k, w):
        # code here
        n = len(arr)
        
        def check(mid):
            diff = [0] * (n + 1)
            used = 0
            current_added = 0
            for i in range(n):
                current_added += diff[i]
                if arr[i] + current_added < mid:
                    needed = mid - (arr[i] + current_added)
                    used += needed
                    if used > k:
                        return False
                    current_added += needed
                    if i + w < n:
                        diff[i + w] -= needed
            return True

        low, high = min(arr), min(arr) + k
        ans = low
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans