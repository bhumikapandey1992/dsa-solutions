# 918. Maximum Sum Circular Subarray — Quick Note

There are two possible answers:

```text
normal maximum   = maximum Kadane
circular maximum = total sum - minimum Kadane
```

Necklace analogy: the wrapping answer keeps the whole circular necklace and cuts out its worst consecutive section.

```python
if global_max < 0:
    return global_max

return max(global_max, total_sum - global_min)
```

The all-negative guard prevents `total_sum - global_min` from removing the entire array and incorrectly returning `0` for an empty subarray.

Time: `O(n)` | Space: `O(1)`
