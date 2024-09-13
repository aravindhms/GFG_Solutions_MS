#User function Template for python3
class Solution:
	def minOperations(self, str1, str2):
        m = len(str1)
        n = len(str2)

        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lcs_length = dp[m][n]

        deletions = m - lcs_length
        insertions = n - lcs_length

        return deletions + insertions		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s1, s2 = input().split()
        ob = Solution()
        ans = ob.minOperations(s1, s2)
        print(ans)

# } Driver Code Ends