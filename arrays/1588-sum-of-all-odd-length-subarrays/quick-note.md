# Sum of All Odd Length Subarrays — Quick Revision

- **Pattern:** Contribution counting
- **Analogy:** Count odd-length train photos containing each car.
- **Starting choices:** `i + 1`
- **Ending choices:** `n - i`
- **All containing subarrays:** `(i + 1) * (n - i)`
- **Odd containing subarrays:** `(total_subarrays + 1) // 2`
- **Element contribution:** `value * odd_subarrays`
- **Time:** `O(n)`
- **Extra space:** `O(1)`
- **Common mistake:** Thinking the left and right counts mean only adjacent positions.
- **Memory sentence:** Choose a left frame, choose a right frame, keep odd photos, then multiply value by appearances.
