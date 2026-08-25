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

## Alternative: counting by bound

Let `count(bound)` count subarrays whose maximum is `<= bound`:

```python
return count(right) - count(left - 1)
```

Within `count`, extend a streak while `num <= bound` and add the streak length. Reset it to zero when `num > bound`.

Why subtract `left - 1`? It removes only maximums strictly below `left`; maximums equal to `left` must stay.

Memory rule: **everything at or below `right`, minus everything below `left`.**

Time: `O(n)` | Space: `O(1)`
