#User function Template for python3

class Solution:
    def rearrange(self,arr):
        pos = []
        neg = []

        for num in arr:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)

        i, j, k = 0, 0, 0
        while i < len(pos) and j < len(neg):
            if k % 2 == 0:
                arr[k] = pos[i]
                i += 1
            else:
                arr[k] = neg[j]
                j += 1
            k += 1

        # If there are leftover positive numbers
        while i < len(pos):
            arr[k] = pos[i]
            i += 1
            k += 1

        # If there are leftover negative numbers
        while j < len(neg):
            arr[k] = neg[j]
            j += 1
            k += 1

        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends