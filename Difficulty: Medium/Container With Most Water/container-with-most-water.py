
class Solution:
    def maxWater(self, arr):
        n = len(arr)
        if n < 2:
            return 0

        left, right = 0, n - 1
        max_water = 0

        while left < right:
            # Calculate the area between left and right pointers
            height = min(arr[left], arr[right])
            width = right - left
            max_water = max(max_water, height * width)

            # Move the pointer pointing to the shorter line
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1

        return max_water


#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends