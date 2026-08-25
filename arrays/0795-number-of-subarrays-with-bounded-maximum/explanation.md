# 795. Number of Subarrays with Bounded Maximum

## Problem in simple words

Count the contiguous subarrays whose largest value is within the inclusive range:

```text
left <= maximum <= right
```

We do not need to build every subarray or repeatedly calculate its maximum. We only need to remember two important positions while scanning from left to right.

## Analogy: a road with checkpoints and walls

Imagine each array position is a location on a road:

- A value `< left` is an ordinary road tile. It may be included, but it cannot make a subarray valid by itself.
- A value in `[left, right]` is a **valid checkpoint**. A subarray containing it has a maximum large enough.
- A value `> right` is an **uncrossable wall**. Any subarray containing it has a maximum that is too large.

For every ending position, ask:

> How many starting positions are after the latest wall but still include the latest valid checkpoint?

## The two remembered indices

### `last_invalid`

```python
if val > right:
    last_invalid = idx
```

This remembers the latest value that is too large. A valid subarray must start strictly after this index.

It begins at `-1`, which represents an imaginary boundary immediately before the array.

### `last_valid`

```python
if val >= left:
    last_valid = idx
```

This remembers the latest value that is at least `left`. If it appears after `last_invalid`, it must be within `[left, right]` and can serve as the required maximum.

## Important detail: why is the condition `val >= left`?

A value greater than `right` also satisfies `val >= left`. Therefore, when a value is too large, both indices may become the current index:

```text
last_invalid = idx
last_valid   = idx
```

This is safe. The counting condition then fails:

```python
last_valid > last_invalid  # False because they are equal
```

No invalid subarray is counted. A later value inside `[left, right]` will move `last_valid` beyond the wall and allow counting to begin again.

## Why add `last_valid - last_invalid`?

For a subarray ending at the current index:

- Its start must be after `last_invalid`, or it would contain a value `> right`.
- Its start must be at or before `last_valid`, or it would miss the value that makes its maximum at least `left`.

So the possible starts are:

```text
last_invalid + 1, ..., last_valid
```

The number of integers in that range is:

```text
last_valid - last_invalid
```

That is why the algorithm uses:

```python
cnt += last_valid - last_invalid
```

## Commented solution

```python
class Solution:
    def numSubarrayBoundedMax(
        self, nums: list[int], left: int, right: int
    ) -> int:
        cnt = 0
        last_invalid = -1
        last_valid = -1

        for idx, val in enumerate(nums):
            if val > right:
                last_invalid = idx

            if val >= left:
                last_valid = idx

            if last_valid > last_invalid:
                cnt += last_valid - last_invalid

        return cnt
```

## Complete dry run

```python
nums = [2, 1, 4, 3]
left = 2
right = 3
```

Valid maximums must be `2` or `3`.

Start with:

```text
cnt = 0
last_invalid = -1
last_valid = -1
```

### Index 0, value 2

`2` is not greater than `right`, so there is no new wall.

`2 >= left`, so:

```text
last_valid = 0
```

The valid starts are after `-1` and at or before `0`:

```text
start 0 -> [2]
```

```text
add 0 - (-1) = 1
cnt = 1
```

### Index 1, value 1

`1` is smaller than `left`. It is neither a wall nor a new valid checkpoint, so both remembered indices stay unchanged.

Possible valid subarrays ending here:

```text
start 0 -> [2, 1]
```

`[1]` is not counted because its maximum is below `left`.

```text
add 0 - (-1) = 1
cnt = 2
```

### Index 2, value 4

`4 > right`, so it is a wall:

```text
last_invalid = 2
```

It also satisfies `4 >= left`, so:

```text
last_valid = 2
```

But the indices are equal:

```text
last_valid > last_invalid -> 2 > 2 -> False
```

Add nothing. Every subarray ending at this index contains `4`, so its maximum is too large.

```text
cnt = 2
```

### Index 3, value 3

`3` is not a wall, and `3 >= left`:

```text
last_valid = 3
```

The valid starts must come after the wall at index `2`:

```text
start 3 -> [3]
```

```text
add 3 - 2 = 1
cnt = 3
```

Final answer:

```text
3
```

The three valid subarrays are:

```text
[2]
[2, 1]
[3]
```

## Why we count subarrays ending at each index

Every subarray has exactly one ending index. On each iteration, the formula counts only valid subarrays ending at the current index. Therefore, no subarray is skipped or counted twice.

## Complexity

- Time: `O(n)` because the array is scanned once.
- Space: `O(1)` because only three counters/indices are stored.

## Memory rule

> A value above `right` creates a wall. A value in `[left, right]` creates a valid anchor. For every ending index, count the possible starts between the latest wall and the latest anchor.
