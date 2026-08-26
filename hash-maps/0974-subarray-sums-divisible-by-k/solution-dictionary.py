class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        # Remainder -> number of earlier prefix sums with that remainder.
        # The empty prefix handles valid subarrays beginning at index 0.
        remainder_counts = {0: 1}

        running_sum = 0
        total_subarrays = 0

        for num in nums:
            # 1. Update the cumulative prefix sum.
            running_sum += num

            # 2. Find its position on the remainder clock.
            remainder = running_sum % k

            # 3. Each earlier matching remainder creates a valid subarray.
            if remainder in remainder_counts:
                total_subarrays += remainder_counts[remainder]

            # 4. Record this prefix for future subarrays.
            remainder_counts[remainder] = remainder_counts.get(remainder, 0) + 1

        return total_subarrays
