class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1

        for write in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[write] = nums[left] ** 2
                left += 1
            else:
                result[write] = nums[right] ** 2
                right -= 1

        return result
