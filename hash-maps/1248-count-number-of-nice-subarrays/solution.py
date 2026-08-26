class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        # Frequency of odd counts among earlier prefixes. The empty prefix
        # contains zero odd numbers.
        odd_frequency = {0: 1}

        odd_count = 0
        total_subarrays = 0

        for num in nums:
            # Odd numbers add 1; even numbers add 0.
            odd_count += num % 2

            # Removing an earlier prefix with odd_count - k odd values leaves
            # exactly k odd values in the intervening subarray.
            needed = odd_count - k
            total_subarrays += odd_frequency.get(needed, 0)

            odd_frequency[odd_count] = odd_frequency.get(odd_count, 0) + 1

        return total_subarrays
