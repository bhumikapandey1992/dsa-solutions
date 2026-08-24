class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        total_sum = 0

        for i, value in enumerate(arr):
            # A subarray containing index i can start at any index from 0 to i
            # and end at any index from i to n - 1.
            total_subarrays = (i + 1) * (n - i)

            # Odd and even lengths alternate. Odd lengths receive the extra
            # subarray when the total number of choices is odd.
            odd_subarrays = (total_subarrays + 1) // 2

            # Add this value once for every odd-length subarray containing it.
            total_sum += value * odd_subarrays

        return total_sum
