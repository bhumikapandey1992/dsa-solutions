# 974. Subarray Sums Divisible by K — Quick Note

Two prefix sums with the same remainder differ by a multiple of `k`.

```python
remainder_counts = {0: 1}

running_sum += num
remainder = running_sum % k
answer += remainder_counts.get(remainder, 0)
remainder_counts[remainder] = remainder_counts.get(remainder, 0) + 1
```

`{0: 1}` represents the empty prefix and counts valid subarrays beginning at index `0`.

Array alternative: use `[0] * k` because the only possible Python remainders are `0` through `k - 1`.

Memory rule: **same place on the remainder clock means the distance between visits completes full circles.**

Time: `O(n)` | Space: `O(k)`
