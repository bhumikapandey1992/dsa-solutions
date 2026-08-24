# 525. Contiguous Array

## Problem in simple words

Find the longest contiguous subarray containing the same number of zeros and ones.

## Hiker-altitude analogy

Imagine a hiker walking through the binary array:

```text
1 → one step uphill  → balance +1
0 → one step downhill → balance -1
```

The hiker's altitude is the running balance:

```text
balance = number of 1s seen - number of 0s seen
```

## The key visual idea

> **If the hiker returns to an altitude visited earlier, the journey between those two visits contains exactly as many uphill steps as downhill steps.**
>
> Therefore, that section contains equal numbers of `1`s and `0`s.

Why? Suppose the hiker was at altitude `1`, wandered through several steps, and later returned to altitude `1`:

```text
ending altitude - starting altitude = 1 - 1 = 0
```

The middle journey produced a net change of zero. Every `+1` uphill step was canceled by a `-1` downhill step.

## Visual walkthrough

Use:

```python
nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
```

The hiker's path is:

```text
Altitude
   4 |                         ●
   3 |                    ●         ●
   2 |               ●                   ●
   1 |          ● ─────────────────────────── ●
   0 | ●             ●
  -1 |      ●
     +--------------------------------------------
       Start  1   2   3   4   5   6   7   8   9
       value  0   1   1   1   1   1   0   0   0
```

The hiker reaches altitude `1` at Step 3 and returns to altitude `1` at Step 9.

```text
Step 3 altitude = 1
Step 9 altitude = 1

net change between them = 1 - 1 = 0
```

The six steps between those visits are:

```text
[1, 1, 1, 0, 0, 0]
```

They contain three uphill steps and three downhill steps:

```text
three 1s
three 0s
length = 9 - 3 = 6
```

## Step-by-step hiker notepad

| Step | Array index | Value | Movement | Altitude / balance | Meaning |
|---:|---:|---:|---|---:|---|
| 0 | Before array | — | Start | 0 | Store altitude `0` at index `-1` |
| 1 | 0 | 0 | Down | -1 | First visit to `-1` |
| 2 | 1 | 1 | Up | 0 | Returned to start altitude; length `2` |
| 3 | 2 | 1 | Up | 1 | First visit to altitude `1`; remember it |
| 4 | 3 | 1 | Up | 2 | First visit to `2` |
| 5 | 4 | 1 | Up | 3 | First visit to `3` |
| 6 | 5 | 1 | Up | 4 | First visit to `4` |
| 7 | 6 | 0 | Down | 3 | Returned to `3`; middle length `2` |
| 8 | 7 | 0 | Down | 2 | Returned to `2`; middle length `4` |
| 9 | 8 | 0 | Down | 1 | Returned to Step 3 altitude; length `6` |

## Why equal balances prove equal zeros and ones

Let the balance at an earlier checkpoint be:

```text
earlier balance = ones_before - zeros_before
```

Let the later balance be identical:

```text
later balance = ones_after - zeros_after
```

Subtract the earlier prefix from the later prefix:

```text
later balance - earlier balance = 0
```

That difference is the balance of the middle subarray:

```text
middle ones - middle zeros = 0
```

Therefore:

```text
middle ones = middle zeros
```

This is the same prefix-state idea as repeated remainders: when a running state repeats, the change between the two checkpoints is neutral.

## Why initialize `{0: -1}`?

```python
first_seen = {0: -1}
```

Before taking any steps, the hiker is at altitude `0`. We represent that imaginary checkpoint as index `-1`.

If the hiker returns to altitude `0` at index `1`:

```text
length = 1 - (-1) = 2
```

That correctly recognizes the subarray from index `0` through index `1` without requiring a special condition.

## Why store the first index only?

The goal is the longest subarray. The earliest visit to an altitude produces the largest possible distance when that altitude appears again.

```text
length = current index - earliest index
```

Overwriting an early index with a later one could only shorten future candidates.

## Implementation with comments

```python
class Solution(object):
    def findMaxLength(self, nums):
        first_seen = {0: -1}
        count = 0
        max_len = 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1

            if count in first_seen:
                length = i - first_seen[count]
                max_len = max(max_len, length)
            else:
                first_seen[count] = i

        return max_len
```

## Code dry run for the visual example

Initialize:

```text
first_seen = {0: -1}
count = 0
max_len = 0
```

| Index `i` | `num` | New `count` | Earlier index | Candidate length | `max_len` |
|---:|---:|---:|---:|---:|---:|
| 0 | 0 | -1 | New → store `0` | — | 0 |
| 1 | 1 | 0 | -1 | `1 - (-1) = 2` | 2 |
| 2 | 1 | 1 | New → store `2` | — | 2 |
| 3 | 1 | 2 | New → store `3` | — | 2 |
| 4 | 1 | 3 | New → store `4` | — | 2 |
| 5 | 1 | 4 | New → store `5` | — | 2 |
| 6 | 0 | 3 | 4 | `6 - 4 = 2` | 2 |
| 7 | 0 | 2 | 3 | `7 - 3 = 4` | 4 |
| 8 | 0 | 1 | 2 | `8 - 2 = 6` | 6 |

Return:

```text
6
```

## Complexity

- Time: `O(n)`
- Extra space: `O(n)`

## Edge cases

- `[0, 1]` returns `2`.
- An array containing only zeros or only ones returns `0`.
- Several balanced sections may exist; preserve the longest.
- A balanced section may begin at index `0`, which is why `{0: -1}` matters.

## Common mistakes

- Counting `0` as zero instead of converting it to `-1`.
- Storing the latest index for a balance instead of the earliest.
- Forgetting the imaginary balance-zero checkpoint at index `-1`.
- Returning the number of matching balances rather than the greatest distance.

## What I learned

Turn `1` into an uphill step and `0` into a downhill step. Returning to a previously visited altitude proves that the journey between the visits contains equal numbers of both steps.
