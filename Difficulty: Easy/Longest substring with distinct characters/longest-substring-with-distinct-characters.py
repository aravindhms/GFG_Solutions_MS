#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        n = len(s)
        char_index = {}
        max_length = 0
        start = 0

        for end in range(n):
            if s[end] in char_index:
                start = max(start, char_index[s[end]] + 1)
            char_index[s[end]] = end
            max_length = max(max_length, end - start + 1)

        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends