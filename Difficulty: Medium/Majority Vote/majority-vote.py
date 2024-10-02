class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):
        n = len(nums)
        if n == 0:
            return -1

        # Step 1: Boyer-Moore Voting Algorithm
        candidate1, candidate2, count1, count2 = None, None, 0, 0

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify candidates
        result = []
        if nums.count(candidate1) > n // 3:
            result.append(candidate1)
        if candidate2 is not None and nums.count(candidate2) > n // 3:
            result.append(candidate2)

        return result if result else [-1]        #Your Code goes here.


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends