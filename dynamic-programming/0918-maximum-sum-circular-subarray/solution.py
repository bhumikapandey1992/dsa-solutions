class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total_sum = nums[0]

        # Best ordinary (non-wrapping) subarray.
        current_max = nums[0]
        global_max = nums[0]

        # Worst subarray. Removing it from the total leaves a wrapping subarray.
        current_min = nums[0]
        global_min = nums[0]

        for num in nums[1:]:
            total_sum += num

            # Start a new maximum subarray or extend the previous one.
            current_max = max(num, current_max + num)
            global_max = max(global_max, current_max)

            # Start a new minimum subarray or extend the previous one.
            current_min = min(num, current_min + num)
            global_min = min(global_min, current_min)

        # With all-negative values, removing the minimum subarray would remove
        # the whole array and incorrectly create an empty subarray with sum 0.
        if global_max < 0:
            return global_max

        normal_max = global_max
        circular_max = total_sum - global_min

        return max(normal_max, circular_max)
