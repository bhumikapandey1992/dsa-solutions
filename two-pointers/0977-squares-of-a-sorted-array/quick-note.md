# Squares of a Sorted Array — Quick Revision

- **Pattern:** Two pointers from opposite ends
- **Recognition clue:** Squaring a sorted array disrupts order around negative values.
- **Simple version:** Square everything and sort in `O(n log n)`.
- **Optimal idea:** The largest absolute value is at one of the two ends.
- **Write direction:** Fill the result from right to left.
- **Move:** Advance the pointer whose square was placed.
- **Optimal time:** `O(n)`
- **Extra space:** `O(n)` for the result
- **Common mistake:** Comparing raw values instead of absolute values or squares.
- **Memory sentence:** Largest square comes from an end, so build backward.
