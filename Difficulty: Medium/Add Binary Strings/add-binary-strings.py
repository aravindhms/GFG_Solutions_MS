#User function Template for python3
class Solution:
	def addBinary(self, s1, s2):
        # Convert binary strings to integers, add them, and convert the result back to binary
        result = bin(int(s1, 2) + int(s2, 2))[2:]
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends