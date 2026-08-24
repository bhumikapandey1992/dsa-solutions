# Minimum Size Subarray Sum — Quick Revision

- **Pattern:** Variable-size sliding window
- **Analogy:** Stretch and shrink an elastic rubber band over positive blocks.
- **Expand:** Add `nums[right]`.
- **Shrink condition:** While `current_sum >= target`.
- **Measure:** `right - left + 1`
- **Shrink:** Subtract `nums[left]`, then increment `left`.
- **No solution:** Return `0` if the minimum remains infinity.
- **Time:** `O(n)` because each pointer moves only forward.
- **Extra space:** `O(1)`
- **Common mistake:** Shrinking once with `if` instead of repeatedly with `while`.
- **Memory sentence:** Stretch until valid, then shrink while valid.
