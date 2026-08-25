# 402. Remove K Digits — Quick Note

Use a monotonic increasing stack:

```python
while k > 0 and stack and stack[-1] > digit:
    stack.pop()
    k -= 1
```

A smaller digit should move left because earlier positions have greater place value.

If `k` remains, remove the last `k` digits. Then join the stack, strip leading zeroes, and return `"0"` if nothing remains.

Memory rule: **pop a larger digit before a smaller digit; trim leftover removals from the end.**

Time: `O(n)` | Space: `O(n)`
