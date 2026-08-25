# Subarray Product Less Than K — Quick Revision

- **Pattern:** Variable-size sliding window
- **Requirement:** All values are positive.
- **Edge case:** Return `0` when `k <= 1`.
- **Expand:** Multiply by `nums[right]`.
- **Shrink:** While product `>= k`, divide out `nums[left]`.
- **Division:** Use `//` because the removed value is an exact factor.
- **Count:** Add `right - left + 1` valid suffixes ending at `right`.
- **Time:** `O(n)`
- **Extra space:** `O(1)`
- **Common mistake:** Using floating-point `/` or shrinking only once.
- **Memory sentence:** Shrink to a valid product, then count every valid start for this right endpoint.
