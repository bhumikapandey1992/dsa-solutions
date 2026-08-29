# 15. 3Sum — Quick Note

1. Sort the array.
2. Fix `nums[i]`.
3. Search after it with `left = i + 1` and `right = n - 1`.
4. Move `left` when the sum is too small and `right` when it is too large.
5. Skip duplicate fixed and pointer values.

```python
if total < 0:
    left += 1
elif total > 0:
    right -= 1
else:
    result.append([nums[i], nums[left], nums[right]])
```

After sorting, `nums[i] > 0` means every available value is positive, so `break` is safe. Do not break at zero because `[0,0,0]` is valid.

Memory rule: **fix one number, then squeeze the other two pointers toward a sum of zero.**

Time: `O(n²)` | Extra space: `O(1)` excluding sorting and output.
