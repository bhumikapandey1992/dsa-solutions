# 523. Continuous Subarray Sum

## Problem in simple words

Determine whether `nums` contains a contiguous subarray of at least two elements whose sum is a multiple of `k`.

```text
subarray sum = k × some integer
```

## Odometer-and-clock analogy

Imagine driving along a road. The running prefix sum is your odometer: it records the total distance traveled from the beginning.

At each checkpoint, you also look at a clock with exactly `k` positions. Instead of recording the entire mileage, you record where the mileage lands on this clock:

```python
remainder = running_sum % k
```

If the clock shows the same position at two checkpoints, the distance traveled between them completed one or more full trips around the clock.

## The central idea — highlight this

> **SAME REMAINDER = A CLEAN MULTIPLE BETWEEN THE CHECKPOINTS**
>
> If two prefix sums leave the same remainder after division by `k`, subtracting them cancels that identical leftover. The subarray between those prefix sums therefore has remainder zero and is divisible by `k`.

### Concrete rope example

Suppose the two prefix sums are:

```text
Earlier checkpoint: 17
Later checkpoint:   29
k = 12
```

Their remainders are identical:

```text
17 % 12 = 5
29 % 12 = 5
```

Both distances contain complete packets of `12` plus the same leftover `5`:

```text
17 = 1 × 12 + 5
29 = 2 × 12 + 5
```

Subtract the earlier prefix from the later prefix:

```text
29 - 17
= (2 × 12 + 5) - (1 × 12 + 5)
= 2 × 12 - 1 × 12 + 5 - 5
= 1 × 12
= 12
```

The two leftover `5`s cancel. Only a clean packet of `12` remains.

> **The repeated remainder is not the answer itself. It is proof that the distance between the two checkpoints has no remainder.**

### General mathematical proof

If two prefix sums have the same remainder `r`, they can be written as:

```text
earlier_prefix = a × k + r
later_prefix   = b × k + r
```

The middle subarray sum is their difference:

```text
later_prefix - earlier_prefix
= (b × k + r) - (a × k + r)
= (b - a) × k
```

The remainder disappears:

```text
r - r = 0
```

Therefore, the middle sum is guaranteed to be a multiple of `k`.

### Memory sentence

> Same clock position twice means the journey between those visits completed full laps.

## Why prefix sums identify the middle subarray

A prefix sum measures from the beginning through the current index.

If:

```text
prefix at index 0 = 23
prefix at index 2 = 29
```

then subtracting removes everything through index `0`:

```text
29 - 23 = 6
```

That difference is the sum from index `1` through index `2`.

```text
nums = [23, 2, 4, ...]
             └──┘
             2 + 4 = 6
```

## The remainder map

```python
first_index = {0: -1}
```

The map stores:

```text
remainder → first index where that remainder appeared
```

When the same remainder appears again, the map gives the earlier checkpoint needed to define the middle subarray.

## Why initialize `{0: -1}`?

Before reading any array values, the prefix sum is conceptually zero:

```text
prefix sum = 0
remainder = 0 % k = 0
```

Store that imaginary checkpoint at index `-1`:

```python
first_index = {0: -1}
```

This lets the normal distance calculation detect a valid subarray beginning at index `0`.

For example, if remainder `0` appears at index `1`:

```text
length = 1 - (-1) = 2
```

The valid subarray covers indexes `0` and `1`. No special case is needed.

## Why check `i - first_index[remainder] >= 2`?

The problem requires at least two elements.

If the earlier equal remainder occurred at index `j`, the subarray begins at `j + 1` and ends at `i`. Its length is:

```text
i - (j + 1) + 1 = i - j
```

Therefore:

```python
i - first_index[remainder] >= 2
```

directly checks the required length.

## Why store only the first occurrence?

The earliest index gives the largest possible future distance.

Suppose remainder `5` appears at indexes `0`, `1`, and `3`:

```text
index:     0  1  2  3
remainder: 5  5  3  5
```

At index `1`, the distance from the first occurrence is only:

```text
1 - 0 = 1 → too short
```

Do not overwrite index `0`. When remainder `5` appears at index `3`:

```text
3 - 0 = 3 → valid
```

Keeping the oldest checkpoint maximizes the chance of satisfying the length rule.

## Implementation with comments

```python
class Solution(object):
    def checkSubarraySum(self, nums, k):
        # Map each remainder to the first index where it appeared.
        # Remainder 0 exists at index -1 before the array begins.
        first_index = {0: -1}
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += num
            remainder = running_sum % k

            if remainder in first_index:
                # Equal remainders guarantee that the sum between the two
                # checkpoints is divisible by k. It must contain 2+ elements.
                if i - first_index[remainder] >= 2:
                    return True
            else:
                # Preserve the earliest index to maximize future distances.
                first_index[remainder] = i

        return False
```

## Complete dry run

```python
nums = [23, 2, 4, 6, 7]
k = 6
```

Initialize:

```text
first_index = {0: -1}
running_sum = 0
```

### Index `0`, value `23`

```text
running_sum = 23
remainder = 23 % 6 = 5
```

Remainder `5` has not appeared, so store:

```text
first_index = {0: -1, 5: 0}
```

### Index `1`, value `2`

```text
running_sum = 23 + 2 = 25
remainder = 25 % 6 = 1
```

Store the new remainder:

```text
first_index = {0: -1, 5: 0, 1: 1}
```

### Index `2`, value `4`

```text
running_sum = 25 + 4 = 29
remainder = 29 % 6 = 5
```

Remainder `5` was first seen at index `0`.

This repeated remainder proves:

```text
29 = 4 × 6 + 5
23 = 3 × 6 + 5

29 - 23 = (4 × 6 + 5) - (3 × 6 + 5)
        = 6
```

The shared leftover `5` cancels, so the middle subarray is divisible by `6`.

Check its length:

```text
2 - 0 = 2
```

It contains two elements, so return `True`:

```text
nums[1:3] = [2, 4]
2 + 4 = 6
```

## Complexity

- Time: `O(n)`
- Extra space: `O(min(n, k))`

The map stores at most one index per distinct remainder and never more entries than processed array positions.

## Common mistakes

- Memorizing “repeated remainder” without understanding that identical leftovers cancel during prefix subtraction.
- Storing the latest remainder index instead of preserving the first.
- Forgetting the minimum subarray length of two.
- Omitting the `{0: -1}` checkpoint and missing subarrays beginning at index `0`.
- Storing full prefix sums when only their remainder classes are needed.

## What I learned

Two prefix totals at the same position on the `k`-hour clock contain the same leftover. Subtracting them cancels that leftover, leaving only complete multiples of `k` in the subarray between them.
