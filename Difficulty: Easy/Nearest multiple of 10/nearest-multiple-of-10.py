#User function Template for python3
import math
class Solution:
    def roundToNearest (self, st) : 
        n=len(st)
        if st[-1]<="5":
            return st[:n-1]+"0"
        carry=1
        st=list(st)
        st[-1]="0"
        for i in range(n-2,-1,-1):
            if st[i]!="9":
                st[i]=str(int(st[i])+1)
                carry=0
                break
            else:
                st[i]="0"
        if carry==1:
            return "1"+"".join(st)
        return "".join(st)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)

# } Driver Code Ends