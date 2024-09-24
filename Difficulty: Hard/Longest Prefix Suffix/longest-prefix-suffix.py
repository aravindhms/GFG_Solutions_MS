#User function Template for python3

class Solution:
	def lps(self, str):
		# code here
        n = len(str)
        lps = [0] * n
        length = 0
        i = 1

        while i < n:
            if str[i] == str[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
                
        return lps[n - 1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.lps(s)
        print(answer)

# } Driver Code Ends