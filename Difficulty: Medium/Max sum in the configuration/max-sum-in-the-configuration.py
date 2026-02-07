class Solution:
    def maxSum(self, arr): 
        # Code here
        n = len(arr)
        total_sum = sum(arr)
        current_val = sum(i * arr[i] for i in range(n))
        max_val = current_val
        
        for k in range(1, n):
            current_val = current_val + total_sum - n * arr[n - k]
            max_val = max(max_val, current_val)
            
        return max_val