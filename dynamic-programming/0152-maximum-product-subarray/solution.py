class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0

        # Initialize all tracking values with the first number.
        global_max = nums[0]

        # Largest product of a subarray that must end at the current position.
        current_max = nums[0]

        # Smallest product of a subarray that must end at the current position.
        # A later negative number can turn this negative valley into a peak.
        current_min = nums[0]

        # Process the remaining numbers.
        for i in range(1, len(nums)):
            num = nums[i]

            # Multiplication by a negative reverses numeric order. The previous
            # minimum can become the new maximum, and vice versa.
            if num < 0:
                current_max, current_min = current_min, current_max

            # Either start a new subarray at num or extend the best previous
            # product ending immediately before this position.
            current_max = max(num, current_max * num)

            # Preserve the smallest product because another negative number
            # could turn it into a large positive product later.
            current_min = min(num, current_min * num)

            # Record the best product found anywhere in the array.
            global_max = max(global_max, current_max)

        return global_max
