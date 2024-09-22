#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        n = len(arr)
        total_sum = n * (n + 1) // 2
        total_square_sum = n * (n + 1) * (2 * n + 1) // 6

        actual_sum = sum(arr)
        actual_square_sum = sum(x * x for x in arr)

        diff_sum = total_sum - actual_sum  # A - B
        diff_square_sum = total_square_sum - actual_square_sum  # A^2 - B^2

        sum_AB = diff_square_sum // diff_sum  # A + B

        A = (diff_sum + sum_AB) // 2
        B = sum_AB - A

        return B, A
      # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends