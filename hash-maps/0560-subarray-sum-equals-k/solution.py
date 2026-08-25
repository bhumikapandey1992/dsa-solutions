from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        # Store how many times each prefix sum has appeared.
        prefix_count = defaultdict(int)

        # One empty prefix with sum 0 exists before the array begins.
        prefix_count[0] = 1

        current_sum = 0
        total_subarrays = 0

        for num in nums:
            current_sum += num

            # We need an earlier prefix where:
            # current_sum - earlier_prefix = k.
            needed = current_sum - k

            # Every earlier occurrence creates a different valid subarray.
            if needed in prefix_count:
                total_subarrays += prefix_count[needed]

            # Record this prefix only after counting earlier matches.
            prefix_count[current_sum] += 1

        return total_subarrays
