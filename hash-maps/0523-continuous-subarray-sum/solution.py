class Solution(object):
    def checkSubarraySum(self, nums, k):
        # Map each remainder to the first index where it appeared.
        # Remainder 0 exists at index -1 before the array begins.
        first_index = {0: -1}
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += num
            remainder = running_sum % k

            if remainder in first_index:
                # Equal remainders guarantee that the sum between the two
                # checkpoints is divisible by k. It must contain 2+ elements.
                if i - first_index[remainder] >= 2:
                    return True
            else:
                # Preserve the earliest index to maximize future distances.
                first_index[remainder] = i

        return False
