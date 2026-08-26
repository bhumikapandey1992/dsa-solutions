from collections import deque


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        # Store indices. max_q decreases by value; min_q increases by value.
        max_q = deque()
        min_q = deque()

        left = 0
        total_subarrays = 0

        for right in range(len(nums)):
            # Remove values that cannot become the maximum while nums[right]
            # remains in the window.
            while max_q and nums[max_q[-1]] <= nums[right]:
                max_q.pop()
            max_q.append(right)

            # Remove values that cannot become the minimum while nums[right]
            # remains in the window.
            while min_q and nums[min_q[-1]] >= nums[right]:
                min_q.pop()
            min_q.append(right)

            # The deque fronts expose the current maximum and minimum.
            while nums[max_q[0]] - nums[min_q[0]] > 2:
                left += 1

                # Discard an index as soon as it leaves the window.
                if max_q[0] < left:
                    max_q.popleft()
                if min_q[0] < left:
                    min_q.popleft()

            # Every suffix of the valid window ending at right is also valid.
            total_subarrays += right - left + 1

        return total_subarrays
