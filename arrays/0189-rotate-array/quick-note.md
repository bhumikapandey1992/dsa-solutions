# Rotate Array — Quick Revision

- **Pattern:** In-place array reversal
- **Recognition clue:** Rotate an array with `O(1)` extra space.
- **Normalize:** `k %= n`
- **Final grouping:** Last `k` elements followed by the first `n - k` elements.
- **Step 1:** Reverse the entire array.
- **Step 2:** Reverse indexes `0` through `k - 1`.
- **Step 3:** Reverse indexes `k` through `n - 1`.
- **Time:** `O(n)`
- **Extra space:** `O(1)`
- **Common mistake:** Forgetting to normalize a large `k`.
- **Memory sentence:** Reverse everything, repair the rotated front, then repair the remaining back.
