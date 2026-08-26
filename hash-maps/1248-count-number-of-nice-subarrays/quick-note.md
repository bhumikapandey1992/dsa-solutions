# 1248. Count Number of Nice Subarrays — Quick Note

Transform conceptually: odd becomes `1`, even becomes `0`. Then count subarrays with transformed sum `k`.

```python
odd_frequency = {0: 1}
odd_count += num % 2
needed = odd_count - k
answer += odd_frequency.get(needed, 0)
odd_frequency[odd_count] = odd_frequency.get(odd_count, 0) + 1
```

`{0: 1}` represents the empty prefix and counts valid subarrays beginning at index `0`.

Memory rule: **current red-bead count minus `k` tells us which earlier count we need.**

Time: `O(n)` | Space: `O(n)`
