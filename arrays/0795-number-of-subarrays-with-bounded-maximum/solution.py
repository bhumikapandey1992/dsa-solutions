class Solution:
    def numSubarrayBoundedMax(
        self, nums: list[int], left: int, right: int
    ) -> int:
        cnt = 0
        # Most recent index whose value was too large (> right).
        # A valid subarray cannot cross this boundary.
        last_invalid = -1

        # Most recent index whose value was large enough (>= left).
        # When it is after last_invalid, it is guaranteed to be in [left, right].
        last_valid = -1

        for idx, val in enumerate(nums):
            # This value is too large and breaks every subarray crossing it.
            if val > right:
                last_invalid = idx

            # This value can provide the required maximum of at least left.
            if val >= left:
                last_valid = idx

            # Choose any starting index after last_invalid and at or before
            # last_valid. Each choice makes a valid subarray ending at idx.
            if last_valid > last_invalid:
                cnt += last_valid - last_invalid

        return cnt
