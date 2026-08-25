class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        total_sum = 0

        # Stack stores (index, value) pairs in increasing value order.
        stack = []

        # The final 0 is smaller than every positive array value. It forces all
        # remaining values to pop so their contributions are calculated.
        extended_arr = arr + [0]

        for curr_idx, curr_val in enumerate(extended_arr):
            # curr_val is the first strictly smaller value on the right of
            # every larger value popped from the stack.
            while stack and stack[-1][1] > curr_val:
                popped_idx, popped_val = stack.pop()

                # Choices for the subarray's right endpoint.
                right_count = curr_idx - popped_idx

                # After the pop, the new stack top is the previous value that
                # is less than or equal to popped_val. Index -1 represents an
                # imaginary boundary just before the array.
                left_idx = stack[-1][0] if stack else -1
                left_count = popped_idx - left_idx

                # Every left choice pairs with every right choice.
                total_sum += popped_val * left_count * right_count
                total_sum %= MOD

            stack.append((curr_idx, curr_val))

        return total_sum
