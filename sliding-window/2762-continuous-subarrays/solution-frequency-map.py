class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        counts = {}
        left = 0
        total_subarrays = 0

        for right in range(len(nums)):
            counts[nums[right]] = counts.get(nums[right], 0) + 1

            # Shrink until the current maximum and minimum differ by at most 2.
            while max(counts) - min(counts) > 2:
                counts[nums[left]] -= 1
                if counts[nums[left]] == 0:
                    del counts[nums[left]]
                left += 1

            total_subarrays += right - left + 1

        return total_subarrays
