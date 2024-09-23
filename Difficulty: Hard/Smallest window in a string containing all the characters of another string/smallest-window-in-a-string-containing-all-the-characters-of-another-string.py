from collections import Counter#User function Template for python3


class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        if len(p) > len(s):
            return "-1"
    
        p_count = Counter(p)
        s_count = Counter()

        start, min_len, min_start = 0, float('inf'), 0
        have, need = 0, len(p_count)

        for end in range(len(s)):
            char = s[end]
            s_count[char] += 1
        
            if char in p_count and s_count[char] == p_count[char]:
                have += 1
        
            while have == need:
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    min_start = start
            
                s_count[s[start]] -= 1
                if s[start] in p_count and s_count[s[start]] < p_count[s[start]]:
                    have -= 1
                start += 1

        return s[min_start:min_start + min_len] if min_len != float('inf') else "-1"
    #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends