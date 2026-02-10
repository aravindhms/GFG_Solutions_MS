class Solution:
    def kokoEat(self, arr, k):
        # Code here
        low = 1
        high = max(arr)
        ans = high
        
        while low <= high:
            mid = low + (high - low) // 2
            
            hours_needed = 0
            for pile in arr:
                hours_needed += math.ceil(pile / mid)
            
            if hours_needed <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
        