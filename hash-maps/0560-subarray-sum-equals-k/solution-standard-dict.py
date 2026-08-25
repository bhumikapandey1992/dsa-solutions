class Solution(object):
    def subarraySum(self, nums, k):
        prefix_count = {0: 1}
        running_sum = 0
        subarray_count = 0

        for num in nums:
            running_sum += num
            needed = running_sum - k

            if needed in prefix_count:
                subarray_count += prefix_count[needed]

            prefix_count[running_sum] = (
                prefix_count.get(running_sum, 0) + 1
            )

        return subarray_count
