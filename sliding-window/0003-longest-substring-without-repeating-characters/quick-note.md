# 3. Longest Substring Without Repeating Characters — Quick Note

Set window:

```python
while s[right] in chars:
    chars.remove(s[left])
    left += 1

chars.add(s[right])
answer = max(answer, right - left + 1)
```

The set always contains exactly the unique characters in the current window.

Last-seen alternative: jump directly with `left = max(left, last_seen[char] + 1)`.

Memory rule: **expand right; when a duplicate enters, move left until only one copy remains. Never move left backward.**

Time: `O(n)` | Space: `O(character set size)`
