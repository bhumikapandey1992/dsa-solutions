# 567. Permutation in String

## Problem in simple words

Return `True` when `s2` contains a substring that is a permutation of `s1`.

A permutation can rearrange characters, but it must contain exactly the same number of every character. It also always has the same length as `s1`.

## Analogy: a fixed-size picture frame

Imagine sliding a picture frame across `s2`. The frame has width `len(s1)` because a permutation cannot be longer or shorter than `s1`.

At every step:

1. Add the new character entering from the right.
2. Remove the old character leaving from the left.
3. Compare the frame's character inventory with the inventory of `s1`.

Matching inventories mean the framed substring is a permutation, even when its order differs.

## Why frequencies solve the problem

For:

```text
s1 = ab
```

Both valid arrangements have this inventory:

```text
a: 1
b: 1
```

So both `ab` and `ba` match the same frequency array. We never need to generate the permutations themselves.

## Why use arrays of size 26?

The problem contains lowercase English letters. Map each character to an array index:

```text
a -> 0
b -> 1
...
z -> 25
```

The mapping is:

```python
ord(char) - ord("a")
```

For example, `c` maps to index `2`.

## Important lines

### Reject an impossible size

```python
if len(s1) > len(s2):
    return False
```

There is no room in `s2` for a substring of length `len(s1)`.

### Build the target inventory

```python
for char in s1:
    index = ord(char) - ord("a")
    target_count[index] += 1
```

This records exactly how many copies of each letter a valid window needs.

### Add the entering character

```python
entering_index = ord(s2[right]) - ord("a")
window_count[entering_index] += 1
```

Every movement of `right` introduces one new letter into the picture frame.

### Remove the leaving character

```python
if right >= window_size:
    leaving_char = s2[right - window_size]
    leaving_index = ord(leaving_char) - ord("a")
    window_count[leaving_index] -= 1
```

Once adding a character would make the frame too large, remove the character exactly `window_size` positions behind `right`.

For window size `2` and `right = 2`, remove index `2 - 2 = 0`. The remaining window covers indices `1` and `2`.

### Compare inventories

```python
if window_count == target_count:
    return True
```

Equal arrays prove that every letter occurs the required number of times. Order is irrelevant.

## Commented solution

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target_count = [0] * 26
        window_count = [0] * 26

        for char in s1:
            index = ord(char) - ord("a")
            target_count[index] += 1

        window_size = len(s1)

        for right in range(len(s2)):
            entering_index = ord(s2[right]) - ord("a")
            window_count[entering_index] += 1

            if right >= window_size:
                leaving_char = s2[right - window_size]
                leaving_index = ord(leaving_char) - ord("a")
                window_count[leaving_index] -= 1

            if window_count == target_count:
                return True

        return False
```

## Complete dry run

```python
s1 = "ab"
s2 = "eidbaooo"
```

Target inventory:

```text
a: 1, b: 1
window_size = 2
```

### `right = 0`, enter `e`

```text
window contents: e
```

The inventory does not match.

### `right = 1`, enter `i`

```text
window contents: ei
window inventory: e:1, i:1
```

No match.

### `right = 2`, enter `d`

Adding `d` temporarily gives `eid`. Remove the character at:

```text
right - window_size = 2 - 2 = 0
```

Remove `e`:

```text
window contents: id
```

No match.

### `right = 3`, enter `b`

Remove the character at index `1`, which is `i`:

```text
window contents: db
```

No match.

### `right = 4`, enter `a`

Remove the character at index `2`, which is `d`:

```text
window contents: ba
window inventory: a:1, b:1
```

The inventory exactly matches `s1`, so return `True`.

Although `ba` is not equal to `ab`, it is a permutation of `ab`.

## Why not generate permutations?

A length-`n` string can have up to `n!` arrangements. Generating them becomes prohibitively expensive.

The frequency window checks only the substrings that actually occur in `s2`.

## Complexity

- Time: `O(len(s1) + 26 * len(s2))`, which is `O(len(s1) + len(s2))` because 26 is constant.
- Space: `O(26)`, which is `O(1)`.

## Memory rule

> Slide a frame the same size as `s1`: add the entering letter, remove the leaving letter, and compare character inventories.
