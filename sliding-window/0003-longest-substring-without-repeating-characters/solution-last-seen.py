class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Character -> most recent index where it appeared.
        last_seen = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            # Jump only when the previous occurrence is still in the window.
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length
