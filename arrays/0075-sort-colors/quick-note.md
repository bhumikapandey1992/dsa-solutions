# Sort Colors — Quick Revision

- **Pattern:** Counting a fixed value range
- **Recognition clue:** The array contains only `0`, `1`, and `2`.
- **Counter:** `counts[color] += 1`
- **Meaning:** Index `0`, `1`, or `2` stores that color's frequency.
- **Zeros:** `nums[:red]`
- **Ones:** `nums[red:red + white]`
- **Twos:** `nums[red + white:]`
- **Time:** `O(n)`
- **Counter space:** `O(1)`
- **Common mistake:** Forgetting that the white section ends at `red + white`.
- **Memory sentence:** Count each color, then paint three consecutive sections.
