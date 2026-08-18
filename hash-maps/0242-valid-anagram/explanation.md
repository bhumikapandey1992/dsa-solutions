# 242. Valid Anagram

## Problem in simple words

Determine whether two strings are anagrams.

Two strings are anagrams when they contain exactly the same letters with exactly the same frequencies, even if those letters appear in a different order.

```text
"anagram" and "nagaram" → True
"rat" and "car"         → False
```

## Two conditions must be true

For `s` and `t` to be anagrams:

1. They must have the same length.
2. Every letter must occur the same number of times in both strings.

The solution checks both conditions using a fixed array of 26 counters—one counter for every lowercase English letter.

## Full analogy: a 26-drawer letter ledger

Imagine a cabinet containing one drawer for each letter:

```text
Letter:  a  b  c  d  e  f  ...  x  y  z
Index:   0  1  2  3  4  5  ... 23 24 25
Count:   0  0  0  0  0  0  ...  0  0  0
```

We process both words together:

- when a letter appears in `s`, put one token into its drawer: `+1`;
- when a letter appears in `t`, remove one token from its drawer: `-1`.

If the strings contain exactly the same letters, every deposit is canceled by a matching withdrawal. All drawers finish at zero.

```text
s deposits letters       +1
t withdraws letters      -1
                         ───
same frequencies          0
```

If even one drawer is non-zero, one string contains more copies of that letter than the other.

## Why check the lengths first?

Different-length strings cannot contain the same total number of characters.

```text
s = "ab"     length 2
t = "aab"    length 3
```

They cannot be anagrams, so we return immediately:

```python
if len(s) != len(t):
    return False
```

This also makes it safe to use the same index `i` for both strings in one loop.

## Mapping letters to array indexes

Python’s `ord` function returns the numeric Unicode value of a character. Lowercase English letters have consecutive numeric values.

```text
ord("a") - ord("a") = 0
ord("b") - ord("a") = 1
ord("c") - ord("a") = 2
...
ord("z") - ord("a") = 25
```

Therefore:

```python
ord(character) - ord("a")
```

converts any lowercase letter into the correct index of the 26-slot array.

## Complete visual dry run: `"anagram"` and `"nagaram"`

Only the relevant letter drawers are shown below.

Start:

```text
Drawer:   a   g   m   n   r
Count:    0   0   0   0   0
```

At every index, add the letter from `s` and subtract the letter from `t`:

```text
i   s[i] action    t[i] action    Relevant result
-----------------------------------------------------------
0     a    +1        n    -1      a:+1, n:-1
1     n    +1        a    -1      a: 0, n: 0
2     a    +1        g    -1      a:+1, g:-1
3     g    +1        a    -1      a: 0, g: 0
4     r    +1        r    -1      r: 0
5     a    +1        a    -1      a: 0
6     m    +1        m    -1      m: 0
```

Final ledger:

```text
Drawer:   a   g   m   n   r
Count:    0   0   0   0   0
```

Every drawer is zero, so the strings are anagrams.

## A failing example: `"rat"` and `"car"`

Process both strings:

```text
s = r a t      deposits r, a, t
t = c a r      withdraws c, a, r
```

The matching `a` and `r` cancel, but `t` and `c` do not:

```text
Drawer:   a   c   r   t
Count:    0  -1   0  +1
```

Because at least one counter is non-zero, return `False`.

## Implementation

```python
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1

        return all(x == 0 for x in count)

        # temp="abcdefghijklmnopqrstuvwxyz"
        # for i in temp:
        #     if s.count(i)!=t.count(i):
        #         return False
        # return True
```

## Line-by-line explanation

### Reject different lengths

```python
if len(s) != len(t):
    return False
```

Anagrams must contain the same total number of characters.

### Create the ledger

```python
count = [0] * 26
```

Create one zero-filled counter for every lowercase English letter.

### Process both strings together

```python
for i in range(len(s)):
```

Since the lengths match, position `i` exists in both strings.

### Deposit the letter from `s`

```python
count[ord(s[i]) - ord("a")] += 1
```

Increase the counter belonging to `s[i]`.

### Withdraw the letter from `t`

```python
count[ord(t[i]) - ord("a")] -= 1
```

Decrease the counter belonging to `t[i]`.

The characters at the same position do not need to match. Only the final frequency balance matters.

### Verify every drawer

```python
return all(x == 0 for x in count)
```

`all(...)` returns `True` only when every one of the 26 conditions is true.

```text
all counters are zero     → True
any counter is non-zero   → False
```

## Understanding the commented alternative

The alternative checks every letter separately:

```python
temp = "abcdefghijklmnopqrstuvwxyz"

for letter in temp:
    if s.count(letter) != t.count(letter):
        return False

return True
```

For each of the 26 letters, `s.count(letter)` scans all of `s`, and `t.count(letter)` scans all of `t`.

Because the alphabet size is fixed at 26, this still behaves as `O(n)` asymptotically. However, it performs many repeated scans:

```text
scan both strings for a
scan both strings for b
scan both strings for c
...
scan both strings for z
```

The frequency-array version scans the strings once and is therefore more direct and efficient in practice.

## Why one shared array works

We could create two separate frequency arrays and compare them. The shared array combines both jobs:

```text
frequency in s - frequency in t
```

If the difference for every letter is zero, the frequencies are identical.

## Complexity

Let `n` be the length of each string:

- Time: `O(n)` because the strings are processed once, followed by a fixed check of 26 counters.
- Extra space: `O(1)` because the array always contains exactly 26 integers.

## Common mistakes

- Forgetting to reject strings with different lengths.
- Using the character’s raw `ord` value as an index instead of subtracting `ord("a")`.
- Increasing counts for both strings instead of increasing for one and decreasing for the other.
- Checking counters inside the loop before all characters have had a chance to cancel.
- Comparing only the set of letters, which ignores repeated-character frequencies.
- Assuming characters at matching positions must be equal; anagrams may use a different order.

## What I learned

When two collections should contain identical frequencies, record one as positive contributions and the other as negative contributions. Perfect cancellation proves they match.
