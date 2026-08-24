class Solution(object):
    def findMaxLength(self, nums):
        # Balance 0 exists before the array begins at index -1.
        first_index = {0: -1}
        balance = 0
        max_length = 0

        for i, num in enumerate(nums):
            # Treat 1 as one step uphill and 0 as one step downhill.
            if num == 1:
                balance += 1
            else:
                balance -= 1

            if balance in first_index:
                # Returning to an earlier balance means the section between
                # the two visits contains equal numbers of uphill and downhill
                # steps—therefore equal numbers of 1s and 0s.
                length = i - first_index[balance]
                max_length = max(max_length, length)
            else:
                # Preserve the earliest visit to maximize future distances.
                first_index[balance] = i

        return max_length
