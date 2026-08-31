class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # A permutation of s1 cannot fit inside a shorter s2.
        if len(s1) > len(s2):
            return False

        target_count = [0] * 26
        window_count = [0] * 26

        for char in s1:
            index = ord(char) - ord("a")
            target_count[index] += 1

        window_size = len(s1)

        for right in range(len(s2)):
            # Add the character entering from the right.
            entering_index = ord(s2[right]) - ord("a")
            window_count[entering_index] += 1

            # Once the window would exceed len(s1), remove its oldest char.
            if right >= window_size:
                leaving_char = s2[right - window_size]
                leaving_index = ord(leaving_char) - ord("a")
                window_count[leaving_index] -= 1

            # Equal inventories mean the window is a permutation of s1.
            if window_count == target_count:
                return True

        return False
