# Merge Sorted Array — Quick Revision

- **Pattern:** Three pointers / merge backward
- **Recognition clue:** Two sorted arrays, with extra capacity at the end of the first array.
- **Pointers:** Last valid `nums1` value, last `nums2` value, and last write position.
- **Core idea:** Place the larger remaining value from right to left.
- **Loop condition:** Continue until every `nums2` value has been copied.
- **Why safe:** Backward writes do not overwrite unprocessed `nums1` values.
- **Time:** `O(m + n)`
- **Extra space:** `O(1)`
- **Common mistake:** Merging forward and overwriting valid elements.
- **Memory sentence:** Compare the largest leftovers and fill the empty slots backward.
