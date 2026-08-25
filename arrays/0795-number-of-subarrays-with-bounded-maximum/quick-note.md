# 795. Number of Subarrays with Bounded Maximum — Quick Note

- `last_invalid`: latest index with `nums[i] > right`; a valid subarray cannot cross it.
- `last_valid`: latest index with `nums[i] >= left`.
- If `last_valid > last_invalid`, the latest qualifying value is after the latest wall and must lie in `[left, right]`.
- Valid starts for a subarray ending at `i` are `last_invalid + 1` through `last_valid`.
- Therefore, add `last_valid - last_invalid`.

```python
if val > right:
    last_invalid = idx
if val >= left:
    last_valid = idx
if last_valid > last_invalid:
    cnt += last_valid - last_invalid
```

Memory rule: **wall, anchor, count the starts between them.**

Time: `O(n)` | Space: `O(1)`
