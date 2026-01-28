class Solution:
    def countSubset(self, arr, k):
        from collections import defaultdict
        
        n = len(arr)
        mid = n // 2
        
        left = arr[:mid]
        right = arr[mid:]
        
        leftSums = []
        rightSums = []
        
        def repeat(a, ind, sumi, store):
            if ind == len(a):
                store.append(sumi)
                return
            
            sumi += a[ind]
            repeat(a, ind + 1, sumi, store)
            sumi -= a[ind]
            
            repeat(a, ind + 1, sumi, store)
        
        repeat(left, 0, 0, leftSums)
        repeat(right, 0, 0, rightSums)
        
        freq = defaultdict(int)
        for s in rightSums:
            freq[s] += 1
        
        ans = 0
        for s in leftSums:
            ans += freq[k - s]
        
        return ans
        # code here
