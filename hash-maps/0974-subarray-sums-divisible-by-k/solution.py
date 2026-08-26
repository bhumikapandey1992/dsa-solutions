class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        # Index r stores how many earlier prefix sums had remainder r.
        remainder_counts = [0] * k
        # The empty prefix has sum 0 and remainder 0.
        remainder_counts[0] = 1

        running_sum = 0
        total_subarrays = 0

        for num in nums:
            running_sum += num
            remainder = running_sum % k

            # Every earlier matching remainder forms one divisible subarray
            # ending at the current position.
            total_subarrays += remainder_counts[remainder]

            # Make this prefix available to future positions.
            remainder_counts[remainder] += 1

        return total_subarrays
