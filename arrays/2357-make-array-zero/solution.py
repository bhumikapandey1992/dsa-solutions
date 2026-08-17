class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        # A set automatically removes duplicates
        # Subtracting {0} ensures we only count strictly positive numbers
        return len(set(nums) - {0})
