class Solution(object):
    def removeKdigits(self, num, k):
        stack = []

        for digit in num:
            # Let a smaller digit move left by deleting larger digits directly
            # before it while removals are still available.
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        # In nondecreasing input, the largest remaining digits are at the end.
        if k > 0:
            stack = stack[:-k]

        result = "".join(stack).lstrip("0")

        return result if result else "0"
