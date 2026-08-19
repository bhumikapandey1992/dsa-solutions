# 88. Merge Sorted Array

## Problem in simple words

Merge the sorted values in `nums2` into `nums1` in non-decreasing order. The first `m` positions of `nums1` contain valid values, and its final `n` positions provide room for the merge.

```text
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6],          n = 3

result = [1, 2, 2, 3, 5, 6]
```

## Intuition

Writing from the beginning could overwrite valid values in `nums1` before they are processed. Instead, fill `nums1` from right to left.

The last valid values of both sorted arrays are their largest remaining values. Compare them, place the larger one into the last open position, and move only the pointer belonging to the value that was placed.

## Pointers

- `p1 = m - 1`: largest unprocessed value in `nums1`
- `p2 = n - 1`: largest unprocessed value in `nums2`
- `write = m + n - 1`: position currently being filled

## Looking closely at the indexing

Use this example:

```text
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6],          n = 3
```

`m = 3` means that only the first three elements of `nums1` are real input values. Their indexes are `0`, `1`, and `2`; the zeros after them are merely empty placeholders.

| Index in `nums1` | Element | Role |
|---:|---:|---|
| 0 | 1 | First valid element |
| 1 | 2 | Second valid element |
| 2 | 3 | Last valid element: index `m - 1 = 3 - 1` |
| 3 | 0 | First empty placeholder |
| 4 | 0 | Second empty placeholder |
| 5 | 0 | Last empty placeholder: index `m + n - 1 = 3 + 3 - 1` |

The `-1` appears because Python uses zero-based indexing. If there are three items, their indexes are `0`, `1`, and `2`, so the last item's index is `3 - 1`.

### Where each pointer begins

```text
nums1 = [1, 2, 3, 0, 0, 0]
                ↑        ↑
             p1 = 2   write = 5

nums2 = [2, 5, 6]
                ↑
             p2 = 2
```

- `p1 = m - 1 = 2` points to `3`, the largest valid value currently in `nums1`.
- `p2 = n - 1 = 2` points to `6`, the largest value currently in `nums2`.
- `write = m + n - 1 = 5` points to the absolute end of `nums1`, where the largest remaining value belongs.

The placeholders are not part of the original sorted data. That is why `p1` starts at `m - 1`, not at the physical end of `nums1`. In contrast, `write` starts at the physical end because that is where we are building the final merged result.

### Pointer memory rule

```text
p1    → end of valid data in nums1
p2    → end of valid data in nums2
write → end of total capacity in nums1
```

After placing a value, move the pointer that supplied it and always move `write` one position left.

## Why compare the values?

Although every value from `nums2` must be copied into `nums1`, the original `nums1` values must also remain in sorted order. The current last position must receive the larger of the two largest remaining values.

```python
if p1 >= 0 and nums1[p1] > nums2[p2]:
    nums1[write] = nums1[p1]
    p1 -= 1
else:
    nums1[write] = nums2[p2]
    p2 -= 1
```

The comparison already decides the `else` case. If the condition is false, either `nums1` has no values left or `nums2[p2] >= nums1[p1]`, so the `nums2` value belongs in the current position.

When a `nums1` value is placed, `p2` does not move. The pending `nums2` value will be compared again and copied later. Therefore, no `nums2` value is lost.

## Dry run

```text
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
```

| Comparison | Value placed | nums1 |
|---|---:|---|
| 3 vs 6 | 6 | `[1, 2, 3, 0, 0, 6]` |
| 3 vs 5 | 5 | `[1, 2, 3, 0, 5, 6]` |
| 3 vs 2 | 3 | `[1, 2, 3, 3, 5, 6]` |
| 2 vs 2 | 2 from `nums2` | `[1, 2, 2, 3, 5, 6]` |

At this point `nums2` is exhausted. The remaining `nums1` values are already in their correct positions.

## Implementation

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1
        p2 = n - 1
        write = m + n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[write] = nums1[p1]
                p1 -= 1
            else:
                nums1[write] = nums2[p2]
                p2 -= 1

            write -= 1
```

## Why does the loop only check `p2`?

Every `nums2` value must be explicitly copied. If `nums1` is exhausted first, the remaining `nums2` values still need copying. If `nums2` is exhausted first, any remaining `nums1` values are already correctly positioned, so no further work is necessary.

## Complexity

- Time: `O(m + n)`
- Extra space: `O(1)`

## Edge cases

- `nums2` is empty: no changes are needed.
- `nums1` has no initial values: copy all of `nums2`.
- Equal values: taking the value from `nums2` is valid and advances `p2`.

## Common mistake

Merging from left to right without extra storage can overwrite an unprocessed `nums1` value.

## What I learned

When an array has empty capacity at the end, merging backward preserves all unprocessed input values.
