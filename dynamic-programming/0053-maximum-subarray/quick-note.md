# Maximum Subarray — Quick Revision

- **Pattern:** Kadane's algorithm / 1D dynamic programming
- **Recognition clue:** Find the maximum sum over a contiguous, non-empty subarray.
- **State:** `current_sum` is the best sum ending at the current index.
- **Transition:** `current_sum = max(num, current_sum + num)`
- **Answer:** Maximum `current_sum` seen during the scan.
- **Initialization:** Use `nums[0]` to support all-negative arrays.
- **Time:** `O(n)`
- **Extra space:** `O(1)`
- **Common mistake:** Initializing to zero and returning an invalid empty subarray for all-negative input.
- **Memory sentence:** At every number, decide whether to extend the old subarray or start fresh here.
