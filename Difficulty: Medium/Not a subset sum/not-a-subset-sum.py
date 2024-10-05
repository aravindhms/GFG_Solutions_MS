#User function Template for python3

class Solution:
    def findSmallest(self, arr):
        n = len(arr)
        res = 1
        
        for i in range(n):
            if arr[i] > res:
                break
            res += arr[i]
        
        return res        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findSmallest(arr)
        print(ans)


if __name__ == "__main__":
    main()

# } Driver Code Ends