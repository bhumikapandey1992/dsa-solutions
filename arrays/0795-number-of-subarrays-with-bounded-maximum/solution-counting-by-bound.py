class Solution:
    def numSubarrayBoundedMax(
        self, nums: list[int], left: int, right: int
    ) -> int:
        def count_valid_subarrays(bound: int) -> int:
            """Count subarrays whose maximum is at most bound."""
            total = 0
            current_streak = 0

            for num in nums:
                if num <= bound:
                    # Every suffix of the current streak ending here is valid.
                    current_streak += 1
                    total += current_streak
                else:
                    # This value is too large, so no valid streak can cross it.
                    current_streak = 0

            return total

        # Remove subarrays with maximum < left from all subarrays with
        # maximum <= right. What remains has maximum in [left, right].
        return count_valid_subarrays(right) - count_valid_subarrays(left - 1)
