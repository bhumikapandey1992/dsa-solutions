# 907. Sum of Subarray Minimums — Quick Note

Use a monotonic nondecreasing stack of `(index, value)`.

When a smaller current value pops `(i, value)`:

```text
right_count = current_index - i
left_count  = i - new_stack_top_index
contribution = value * left_count * right_count
```

If the stack is empty after popping, use left boundary `-1`.

Append a dummy `0` to force every positive value to pop at the end.

Why `>` rather than `>=`? Equal values stay in the stack, making the left boundary non-strict and the right boundary strict so duplicate subarrays have one owner.

Paint analogy: **paint spreads until a wall; left choices × right choices tells how many subarrays that bucket paints as the minimum.**

Time: `O(n)` | Space: `O(n)`
