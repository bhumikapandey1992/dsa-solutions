# 205. Isomorphic Strings

## Problem in simple words

Two strings are isomorphic when the characters in the first string can be consistently replaced to produce the second string.

The mapping must be one-to-one:

- One character from `s` must always map to the same character in `t`.
- Two different characters from `s` cannot map to the same character in `t`.

The order and repetition pattern must remain the same.

## Valid example

```text
s = "egg"
t = "add"
```

The mappings are:

```text
e → a
g → d
g → d
```

Every repeated `g` consistently maps to `d`, so the strings are isomorphic.

## Invalid consistency example

```text
s = "foo"
t = "bar"
```

The first `o` would map to `a`, but the second `o` would need to map to `r`:

```text
o → a
o → r  ← conflict
```

One source character cannot change its destination.

## Why two maps are necessary

Use one mapping in each direction:

```python
s_to_t = {}
t_to_s = {}
```

### Forward map

```text
s_to_t: character from s → character from t
```

This ensures one character from `s` does not map to multiple characters in `t`.

### Reverse map

```text
t_to_s: character from t → character from s
```

This ensures multiple characters from `s` do not map to the same character in `t`.

Consider:

```text
s = "badc"
t = "baba"
```

A forward map alone could appear to allow:

```text
b → b
a → a
d → b  ← b is already used by b
c → a  ← a is already used by a
```

The reverse map detects that `b` and `a` already belong to different source characters.

## Process corresponding characters together

```python
for char_s, char_t in zip(s, t):
```

`zip` pairs characters at the same positions:

```text
s = e g g
t = a d d

pairs: (e, a), (g, d), (g, d)
```

## Check the forward mapping

```python
if char_s in s_to_t and s_to_t[char_s] != char_t:
    return False
```

If `char_s` was seen before, it must still map to the same `char_t`.

Example conflict:

```text
stored:  o → a
current: o → r
```

## Check the reverse mapping

```python
if char_t in t_to_s and t_to_s[char_t] != char_s:
    return False
```

If `char_t` was already used, it must belong to the same `char_s`.

Example conflict:

```text
stored:  b ← b
current: b ← d
```

## Record both directions

When neither check finds a conflict:

```python
s_to_t[char_s] = char_t
t_to_s[char_t] = char_s
```

Recording both directions preserves the one-to-one relationship.

## Dry run: `s = "egg"`, `t = "add"`

Start with:

```text
s_to_t = {}
t_to_s = {}
```

### Pair `e` and `a`

Neither character has a mapping, so record:

```text
s_to_t = {e: a}
t_to_s = {a: e}
```

### Pair `g` and `d`

Neither character has a mapping, so record:

```text
s_to_t = {e: a, g: d}
t_to_s = {a: e, d: g}
```

### Pair `g` and `d` again

Check the stored mappings:

```text
g already maps to d ✓
d already maps from g ✓
```

No conflicts occur, so return `True`.

## Implementation

```python
class Solution(object):
    def isIsomorphic(self, s, t):
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            if char_s in s_to_t and s_to_t[char_s] != char_t:
                return False

            if char_t in t_to_s and t_to_s[char_t] != char_s:
                return False

            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True
```

## Complexity

- Time: `O(n)`
- Extra space: `O(n)` in the general case

The stored mappings are effectively bounded when the character set is fixed.

## Edge cases

- Repeated characters must repeat in the same positions.
- Two source characters cannot share one destination character.
- A character may map to itself.
- Strings containing spaces or other valid characters follow the same logic.

## Common mistakes

- Keeping only `s_to_t` and allowing two source characters to share a target.
- Comparing only character frequencies; equal frequencies do not guarantee the same positional pattern.
- Updating a mapping without first checking for a conflict.

## What I learned

A one-to-one substitution requires consistency in both directions. Maintain a forward map and a reverse map to enforce that bijection.
