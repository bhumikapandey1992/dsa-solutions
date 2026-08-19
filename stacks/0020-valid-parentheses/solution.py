class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # Map each closing bracket to its opening counterpart.
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                # Pop the top element when possible. If the stack is empty,
                # use a dummy character that cannot match an opening bracket.
                top_element = stack.pop() if stack else "#"

                # The most recent opening bracket must match this closer.
                if mapping[char] != top_element:
                    return False
            else:
                # Opening brackets wait on the stack for their matching closer.
                stack.append(char)

        # An empty stack means every opening bracket was matched.
        return len(stack) == 0
