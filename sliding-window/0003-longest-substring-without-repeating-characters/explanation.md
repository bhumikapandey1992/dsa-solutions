# 3. Longest Substring Without Repeating Characters

## Problem in simple words

Find the length of the longest contiguous substring containing no repeated character.

This is a variable-size sliding-window problem:

- expand with `right`;
- shrink with `left` when a duplicate makes the window invalid;
- record the longest valid length.

## Analogy: a duplicate-free train compartment

Imagine characters entering a train compartment from the right. The compartment allows only one copy of each character.

When a duplicate tries to enter, remove passengers from the left until the old copy of that character is gone. Then admit the new character and measure the compartment.

## Solution 1: set-based shrinking window

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        chars = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
```

## Important lines in the set solution

### The current-window inventory

```python
chars = set()
```

The set contains exactly the characters between `left` and `right` after the window is made valid. A set provides fast membership checks.

### Expand from the right

```python
for right in range(len(s)):
```

`right` introduces one new character at a time.

### Shrink while a duplicate exists

```python
while s[right] in chars:
    chars.remove(s[left])
    left += 1
```

If the entering character is already in the set, the current window would contain a duplicate.

Remove the leftmost character and advance `left`. Repeat until the previous copy of `s[right]` has been removed.

We need `while`, not `if`, because the duplicate may not be at the left edge. Several characters might need to leave before reaching it.

### Add only after the window is ready

```python
chars.add(s[right])
```

At this point, the old duplicate is gone. Adding the entering character preserves the no-repetition rule.

### Measure the inclusive window

```python
max_length = max(max_length, right - left + 1)
```

The window includes both endpoints. For `left = 2` and `right = 4`, the indices are `2, 3, 4`, so the length is `4 - 2 + 1 = 3`.

## Complete set-solution dry run

```python
s = "abcabcbb"
```

Start:

```text
chars = {}
left = 0
max_length = 0
```

| Right | Enter | Characters removed | Left after shrinking | Window | Length | Best |
|---:|:---:|---|---:|---|---:|---:|
| 0 | a | none | 0 | `a` | 1 | 1 |
| 1 | b | none | 0 | `ab` | 2 | 2 |
| 2 | c | none | 0 | `abc` | 3 | 3 |
| 3 | a | a | 1 | `bca` | 3 | 3 |
| 4 | b | b | 2 | `cab` | 3 | 3 |
| 5 | c | c | 3 | `abc` | 3 | 3 |
| 6 | b | a, b | 5 | `cb` | 2 | 3 |
| 7 | b | c, b | 7 | `b` | 1 | 3 |

### The important multi-removal step

Before index `6`, the window is:

```text
indices 3..5 -> abc
chars = {a, b, c}
```

The entering character is another `b`. Removing only the leftmost `a` is insufficient because `b` is still present:

```text
remove a -> window bc -> b is still duplicated
remove b -> window c  -> duplicate is gone
add new b -> window cb
```

This demonstrates why the code uses `while`.

The longest length remains `3`.

## Solution 2: last-seen index jump

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length
```

Instead of removing characters one by one, this version remembers the most recent index of each character and jumps `left` directly beyond a duplicate.

## Why check `last_seen[char] >= left`?

Consider:

```python
s = "abba"
```

At the second `b`, `left` moves to index `2`. At the final `a`, the previous `a` was at index `0`, but that occurrence is already outside the current window.

Moving `left` back to index `1` would be incorrect. The condition ensures that only duplicates still inside the current window move `left`.

The same protection can be written as:

```python
left = max(left, last_seen[char] + 1)
```

The essential rule is that `left` never moves backward.

## Comparing both solutions

### Set-based version

- Directly represents the characters inside the window.
- Shrinks one position at a time.
- Often easier to visualize.
- Each character enters and leaves the set at most once, so it is still `O(n)`.

### Last-seen version

- Stores each character's newest index.
- Jumps directly past a duplicate.
- Usually performs fewer individual shrinking operations.
- Also runs in `O(n)`.

Both are optimal and return the same result.

## Edge cases

```text
empty string       -> 0
bbbbb              -> 1
abcdef             -> 6
abba               -> 2
```

Spaces and symbols count as ordinary characters.

## Complexity

- Time: `O(n)` for both solutions.
- Space: `O(min(n, character-set size))`.

## Memory rule

> Expand right. When a duplicate enters, move left until the old copy is outside the window. Measure only after the window is valid again.
