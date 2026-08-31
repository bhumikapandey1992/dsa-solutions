# 567. Permutation in String — Quick Note

Slide a fixed-size window of length `len(s1)` across `s2`.

```python
window_count[ord(s2[right]) - ord("a")] += 1

if right >= len(s1):
    window_count[ord(s2[right - len(s1)]) - ord("a")] -= 1

if window_count == target_count:
    return True
```

A permutation may have a different order, but its 26 character frequencies must exactly match.

Memory rule: **add the entering letter, remove the leaving letter, and compare inventories.**

Time: `O(len(s1) + len(s2))` | Space: `O(1)`
