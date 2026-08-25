# 560. Subarray Sum Equals K

## Problem in simple words

Count how many contiguous subarrays have a sum exactly equal to `k`.

The array may contain positive values, negative values, and zeros. A normal sliding window is unreliable because expanding the window does not always increase its sum.

## Prefix-sum idea

A prefix sum is the total from the beginning of the array through the current position.

If:

```text
current prefix - earlier prefix = k
```

then the elements between those checkpoints form a subarray whose sum is `k`.

Rearrange the equation:

```text
earlier prefix = current prefix - k
```

That produces the lookup used by the code:

```python
needed = current_sum - k
```

## Rope-cutting analogy

Imagine measuring a rope only from its beginning.

At the current checkpoint, the rope measures `10`. You want a middle section measuring `4`.

Ask:

```text
What earlier measurement must I cut away?

10 - earlier measurement = 4
earlier measurement = 10 - 4 = 6
```

If the notepad says an earlier prefix measured `6`, subtracting it leaves a middle section of exactly `4`.

> **At every checkpoint, calculate `current_sum - k` and ask how many times that earlier measurement appeared.**

## Why the map stores frequencies

The map is:

```text
prefix sum → number of times seen
```

The same prefix sum can appear more than once, especially when the array contains zeros or values that cancel each other.

Every occurrence represents a different starting checkpoint, producing a different valid subarray ending at the current position.

For example:

```python
nums = [0, 0]
k = 0
```

The valid subarrays are:

```text
index 0:    [0]
index 1:    [0]
indexes 0–1:[0, 0]
```

There are three answers because prefix sum `0` appears at multiple earlier checkpoints.

## Why initialize `prefix_count[0] = 1`?

Before reading any values, there is one empty prefix with sum zero:

```python
prefix_count[0] = 1
```

This allows the normal formula to detect a valid subarray beginning at index `0`.

Suppose the current prefix sum equals `k`:

```text
needed = current_sum - k
       = k - k
       = 0
```

The initial zero prefix contributes one valid subarray from the beginning through the current position.

## Why count matches before recording the current prefix?

The order is:

```python
total_subarrays += prefix_count[needed]
prefix_count[current_sum] += 1
```

We want earlier prefix checkpoints. Recording the current prefix first could allow the current checkpoint to match itself when `k = 0`, creating an empty subarray. The problem counts non-empty subarrays, so record the current prefix only after counting valid earlier matches.

## Why `defaultdict(int)`?

```python
prefix_count = defaultdict(int)
```

For a missing key, `defaultdict(int)` automatically supplies `0`:

```text
missing prefix count → 0
```

Therefore, this update works without calling `.get()`:

```python
prefix_count[current_sum] += 1
```

The standard dictionary version performs the same update explicitly:

```python
prefix_count[current_sum] = (
    prefix_count.get(current_sum, 0) + 1
)
```

Both implementations have the same algorithm and complexity.

## `defaultdict` implementation with comments

```python
from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        # Store how many times each prefix sum has appeared.
        prefix_count = defaultdict(int)

        # One empty prefix with sum 0 exists before the array begins.
        prefix_count[0] = 1

        current_sum = 0
        total_subarrays = 0

        for num in nums:
            current_sum += num

            # We need an earlier prefix where:
            # current_sum - earlier_prefix = k.
            needed = current_sum - k

            # Every earlier occurrence creates a different valid subarray.
            if needed in prefix_count:
                total_subarrays += prefix_count[needed]

            # Record this prefix only after counting earlier matches.
            prefix_count[current_sum] += 1

        return total_subarrays
```

## Standard dictionary version

```python
class Solution(object):
    def subarraySum(self, nums, k):
        prefix_count = {0: 1}
        running_sum = 0
        subarray_count = 0

        for num in nums:
            running_sum += num
            needed = running_sum - k

            if needed in prefix_count:
                subarray_count += prefix_count[needed]

            prefix_count[running_sum] = (
                prefix_count.get(running_sum, 0) + 1
            )

        return subarray_count
```

## Complete dry run

```python
nums = [1, 1, 1]
k = 2
```

Initialize:

```text
prefix_count = {0: 1}
current_sum = 0
total_subarrays = 0
```

### Read the first `1`

```text
current_sum = 0 + 1 = 1
needed = 1 - 2 = -1
```

`-1` has not appeared, so add no answers.

Record the current prefix:

```text
prefix_count = {0: 1, 1: 1}
```

### Read the second `1`

```text
current_sum = 1 + 1 = 2
needed = 2 - 2 = 0
```

Prefix `0` appeared once:

```text
total_subarrays += 1
total_subarrays = 1
```

This represents the subarray from the beginning:

```text
[1, 1]
```

Record prefix `2`:

```text
prefix_count = {0: 1, 1: 1, 2: 1}
```

### Read the third `1`

```text
current_sum = 2 + 1 = 3
needed = 3 - 2 = 1
```

Prefix `1` appeared once:

```text
total_subarrays += 1
total_subarrays = 2
```

This represents the last two values:

```text
[1, 1]
```

Record prefix `3`, then return:

```text
2
```

## How this differs from problems 523 and 525

All three problems use a repeated prefix state, but the requested result changes what the map stores:

| Problem | Goal | Map value |
|---|---|---|
| 523. Continuous Subarray Sum | Determine whether a valid length-2+ subarray exists | Earliest index |
| 525. Contiguous Array | Find the longest neutral-balance subarray | Earliest index |
| 560. Subarray Sum Equals K | Count every valid subarray | Frequency |

For problem 560, preserving only one index would lose other valid starting checkpoints. We need the number of occurrences.

## Complexity

- Time: `O(n)` average
- Extra space: `O(n)`

## Edge cases

- A valid subarray begins at index `0`.
- Negative numbers make sliding-window logic unreliable but do not affect prefix sums.
- Zeros can produce several identical prefix sums and several valid subarrays.
- `k` may be zero or negative; the subtraction formula still works.

## Common mistakes

- Storing only one prefix index instead of its frequency.
- Forgetting the initial `{0: 1}` frequency.
- Recording the current prefix before counting earlier matches.
- Using a sliding window even though negative numbers may be present.
- Returning the number of unique prefix sums instead of the number of subarrays.

## What I learned

At every checkpoint, look for `current_sum - k`. Each time that earlier prefix occurred creates one different subarray ending here with sum `k`.
