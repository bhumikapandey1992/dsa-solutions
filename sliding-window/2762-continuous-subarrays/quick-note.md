# 2762. Continuous Subarrays — Quick Note

A window is valid when:

```text
maximum - minimum <= 2
```

Use a decreasing deque for the maximum and an increasing deque for the minimum. Their fronts hold the current extremes.

Shrink `left` while the difference exceeds `2`, removing indices that fall outside the window.

After shrinking, add:

```python
right - left + 1
```

Every suffix ending at `right` and starting from `left` through `right` is valid.

Frequency-map alternative: store value counts and use `max(counts) - min(counts)`, but finding those extremes repeatedly is slower.

Deque version: `O(n)` time, `O(n)` space.
