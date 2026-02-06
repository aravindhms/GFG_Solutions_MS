class Solution:
    def smallestDiff(self,a, b, c):
        #code here.
        a.sort()
        b.sort()
        c.sort()
        
        n = len(a)
        i, j, k = 0, 0, 0
        
        min_diff = float('inf')
        min_sum = float('inf')
        res = []
        
        while i < n and j < n and k < n:
            current_min = min(a[i], b[j], c[k])
            current_max = max(a[i], b[j], c[k])
            current_diff = current_max - current_min
            current_sum = a[i] + b[j] + c[k]
            
            if current_diff < min_diff:
                min_diff = current_diff
                min_sum = current_sum
                res = [a[i], b[j], c[k]]
            elif current_diff == min_diff:
                if current_sum < min_sum:
                    min_sum = current_sum
                    res = [a[i], b[j], c[k]]
            
            if a[i] == current_min:
                i += 1
            elif b[j] == current_min:
                j += 1
            else:
                k += 1
                
        res.sort(reverse=True)
        return res
    
