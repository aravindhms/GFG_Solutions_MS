'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getKClosest(self, root, target, k):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.data] + inorder(node.right)
        
        # Step 1: Get sorted array of BST elements
        arr = inorder(root)
        
        # Step 2: Find the index where target fits (binary search)
        import bisect
        idx = bisect.bisect_left(arr, target)
        
        # Step 3: Initialize two pointers around target
        left, right = idx - 1, idx
        result = []
        
        # Step 4: Choose k closest values
        while k > 0:
            if left < 0:
                result.append(arr[right])
                right += 1
            elif right >= len(arr):
                result.append(arr[left])
                left -= 1
            else:
                # Compare absolute differences
                if abs(arr[left] - target) <= abs(arr[right] - target):
                    result.append(arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1
            k -= 1
        
        return result
        
    