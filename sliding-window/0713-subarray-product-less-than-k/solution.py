class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        # Since every element is positive, every non-empty product is at least
        # 1. No product can be strictly below k when k <= 1.
        if k <= 1:
            return 0

        total_count = 0
        current_product = 1
        left = 0

        # Expand the sliding window using the right pointer.
        for right in range(len(nums)):
            current_product *= nums[right]

            # Shrink from the left until the product is valid again.
            while current_product >= k:
                # nums[left] is an exact factor of current_product, so integer
                # division removes it without rounding or floating-point values.
                current_product //= nums[left]
                left += 1

            # Every subarray ending at right and starting from left through
            # right has a product below k.
            total_count += right - left + 1

        return total_count
