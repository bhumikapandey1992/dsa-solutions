# Valid Parentheses — Quick Revision

- **Pattern:** Stack / matching pairs
- **Recognition clue:** Closers must match the most recent unmatched opener.
- **Map:** Closing bracket → required opening bracket
- **Opening bracket:** Push onto the stack.
- **Closing bracket:** Stack must be non-empty and its top must match.
- **Successful match:** Pop the stack.
- **Final check:** Return `not stack`.
- **Time:** `O(n)`
- **Extra space:** `O(n)`
- **Common mistake:** Reading `stack[-1]` before checking for an empty stack.
- **Memory sentence:** The last bracket opened must be the first one closed.
