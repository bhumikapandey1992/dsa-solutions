class Solution(object):
    def findMaxLength(self, nums):
        first_seen = {0: -1}
        count = 0
        max_len = 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1

            if count in first_seen:
                length = i - first_seen[count]
                max_len = max(max_len, length)
            else:
                first_seen[count] = i

        return max_len
