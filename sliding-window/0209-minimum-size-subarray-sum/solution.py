class Solution(object):
    def minSubArrayLen(self, target, nums):
        # Start with infinity because we want to find a smaller valid length.
        min_length = float("inf")
        current_sum = 0
        left = 0

        # Expand the right side of the window one element at a time.
        for right in range(len(nums)):
            current_sum += nums[right]

            # While the window is valid, record its length and shrink it from
            # the left to search for a shorter valid window.
            while current_sum >= target:
                current_length = right - left + 1
                min_length = min(min_length, current_length)

                # Remove the leftmost value before advancing the left pointer.
                current_sum -= nums[left]
                left += 1

        # Infinity means no window ever reached the target.
        return min_length if min_length != float("inf") else 0
