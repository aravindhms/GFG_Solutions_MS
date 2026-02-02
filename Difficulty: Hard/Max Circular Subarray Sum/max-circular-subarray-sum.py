class Solution:
    def maxCircularSum(self, arr):
        # code here
        total_sum = 0
        curr_max, max_sum = 0, float('-inf')
        curr_min, min_sum = 0, float('inf')
        
        for x in arr:
            total_sum += x
            
            curr_max = max(x, curr_max + x)
            max_sum = max(max_sum, curr_max)
            
            curr_min = min(x, curr_min + x)
            min_sum = min(min_sum, curr_min)
            
        if max_sum < 0:
            return max_sum
            
        return max(max_sum, total_sum - min_sum)