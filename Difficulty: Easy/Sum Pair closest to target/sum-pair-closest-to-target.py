#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        if len(arr) < 2:
            return []

        arr.sort()
        left, right = 0, len(arr) - 1
        closest_diff = float('inf')
        best_pair = []

        while left < right:
            current_sum = arr[left] + arr[right]
            diff = abs(target - current_sum)

            if diff < closest_diff or (diff == closest_diff and abs(arr[right] - arr[left]) > abs(best_pair[1] - best_pair[0])):
                closest_diff = diff
                best_pair = [arr[left], arr[right]]

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                break

        return best_pair



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends