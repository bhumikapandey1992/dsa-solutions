class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        stack = []  # (minimum value, number of subarrays in its group)
        ending_sum = 0
        answer = 0

        for num in arr:
            count = 1

            while stack and stack[-1][0] >= num:
                old_minimum, old_count = stack.pop()
                count += old_count
                ending_sum -= old_minimum * old_count

            stack.append((num, count))
            ending_sum += num * count
            answer += ending_sum

        return answer % MOD
