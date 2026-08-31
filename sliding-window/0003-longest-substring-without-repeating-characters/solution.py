class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Contains exactly the characters in the current window.
        chars = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # Shrink until the new character is no longer duplicated.
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
