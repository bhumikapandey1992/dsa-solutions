# 907. Sum of Subarray Minimums

## Problem in simple words

For every contiguous subarray:

1. Find its minimum.
2. Add that minimum to the answer.

Generating every subarray would take `O(n²)`. Instead, we calculate how many subarrays use each number as their chosen minimum.

## Main idea: contribution counting

Suppose `arr[i]` is the minimum in 6 subarrays. Its total contribution is:

```text
arr[i] * 6
```

To find that 6, determine:

- how many valid starting positions exist on its left;
- how many valid ending positions exist on its right.

Every left choice can pair with every right choice:

```text
number of subarrays = left_count * right_count
contribution = value * left_count * right_count
```

## The paint-spread analogy

Imagine every number is a paint bucket. Its paint spreads left and right while that number can remain the minimum.

- A smaller or equal value on the left is the left wall.
- A strictly smaller value on the right is the right wall.
- Between those walls, the number can be selected as the minimum.

The monotonic increasing stack remembers paint buckets that have not found their right wall yet.

When a smaller value appears, it becomes the right wall for every larger value it pops.

## What the stack contains

```python
stack = []  # (index, value)
```

The values remain in nondecreasing order from bottom to top. Each stored value is waiting to discover the first strictly smaller value on its right.

We need the indices because distances determine the number of possible subarray boundaries.

## Why append a dummy zero?

```python
extended_arr = arr + [0]
```

LeetCode guarantees that the original values are positive. Therefore, the final `0` is smaller than every original number.

Some values may never meet a smaller value during the normal scan. The dummy zero acts as a final right wall and forces all of them out of the stack so their contributions are not forgotten.

The dummy is pushed at the end, but its own contribution is zero and is never added.

## Code-to-analogy mapping

### Scan each location

```python
for curr_idx, curr_val in enumerate(extended_arr):
```

Move from one paint bucket to the next, including the final cleanup bucket `0`.

### Detect a right wall

```python
while stack and stack[-1][1] > curr_val:
```

The current paint bucket is strictly smaller than the bucket on top. The top bucket's paint cannot spread through it, so its right boundary is now known.

Use `while` because one small number may stop several larger buckets.

### Select the bucket being measured

```python
popped_idx, popped_val = stack.pop()
```

Remove the bucket whose complete left and right paint range can now be calculated.

### Count right-end choices

```python
right_count = curr_idx - popped_idx
```

The subarray may end at any index from `popped_idx` through `curr_idx - 1`.

```text
popped_idx, ..., curr_idx - 1
```

That gives `curr_idx - popped_idx` choices.

### Find the left wall

```python
left_idx = stack[-1][0] if stack else -1
left_count = popped_idx - left_idx
```

After popping, the new top is the closest remaining value on the left that is less than or equal to `popped_val`.

If the stack is empty, use the imaginary index `-1`, meaning the paint can spread all the way to index `0`.

The subarray may start at any index from `left_idx + 1` through `popped_idx`, giving `popped_idx - left_idx` choices.

### Calculate the contribution

```python
total_sum += popped_val * left_count * right_count
```

Every valid left endpoint pairs with every valid right endpoint. In all those subarrays, `popped_val` is the selected minimum.

### Save a bucket still waiting for its right wall

```python
stack.append((curr_idx, curr_val))
```

The current bucket enters the stack until a smaller value eventually stops it.

## Why `>` rather than `>=`?

Duplicate values require consistent ownership so the same subarray is not counted twice.

This version pops only when:

```python
stack[-1][1] > curr_val
```

Therefore:

- the left boundary may contain an equal value;
- the right boundary must be strictly smaller.

Equal values stay together in the stack. This assigns overlapping subarrays consistently to one copy. The opposite tie rule can also work, but one side must be strict and the other non-strict.

## Full implementation

```python
class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        total_sum = 0
        stack = []
        extended_arr = arr + [0]

        for curr_idx, curr_val in enumerate(extended_arr):
            while stack and stack[-1][1] > curr_val:
                popped_idx, popped_val = stack.pop()
                right_count = curr_idx - popped_idx

                if stack:
                    left_idx = stack[-1][0]
                    left_count = popped_idx - left_idx
                else:
                    left_count = popped_idx - (-1)

                total_sum += popped_val * left_count * right_count
                total_sum %= MOD

            stack.append((curr_idx, curr_val))

        return total_sum
```

## Complete line-by-line dry run

```python
arr = [3, 1, 2]
extended_arr = [3, 1, 2, 0]
```

Initialize:

```text
total_sum = 0
stack = []
```

### Index 0: `curr_val = 3`

Check:

```python
while stack and stack[-1][1] > curr_val:
```

The stack is empty, so nobody is waiting for a right wall. Skip the loop.

Push:

```python
stack.append((0, 3))
```

Paint meaning: bucket `3` begins waiting for its right wall.

```text
stack = [(0, 3)]
total_sum = 0
```

Its contribution is not lost; it will be calculated when its right wall becomes known.

### Index 1: `curr_val = 1`

Check:

```text
3 > 1 -> True
```

The `1` is the right wall for `3`.

Pop the target bucket:

```python
popped_idx, popped_val = stack.pop()
```

```text
popped_idx = 0
popped_val = 3
```

Right choices:

```text
right_count = curr_idx - popped_idx
            = 1 - 0
            = 1
```

The right endpoint can only be index `0`.

The stack is now empty, so the imaginary left wall is `-1`:

```text
left_count = popped_idx - (-1)
           = 0 - (-1)
           = 1
```

The left endpoint can only be index `0`.

Contribution:

```text
3 * 1 * 1 = 3
total_sum = 3
```

So `3` is the minimum of exactly one owned subarray:

```text
[3]
```

After the `while` loop, push `1`:

```text
stack = [(1, 1)]
```

### Index 2: `curr_val = 2`

Check:

```text
1 > 2 -> False
```

`2` does not stop `1`; the paint from `1` can spread through `2`.

Push `2`:

```text
stack = [(1, 1), (2, 2)]
total_sum = 3
```

### Index 3: `curr_val = 0`

This is the dummy cleanup value. Because it is smaller than every original value, it forces all remaining buckets to reveal their right boundaries.

#### First while-loop cycle: process `2`

```text
2 > 0 -> True
```

Pop:

```text
popped_idx = 2
popped_val = 2
```

Right choices:

```text
right_count = 3 - 2 = 1
```

The new stack top is `(1, 1)`, so index `1` is the left wall:

```text
left_count = 2 - 1 = 1
```

Contribution:

```text
2 * 1 * 1 = 2
total_sum = 3 + 2 = 5
```

`2` owns one subarray:

```text
[2]
```

#### Second while-loop cycle: process `1`

```text
1 > 0 -> True
```

Pop:

```text
popped_idx = 1
popped_val = 1
```

Right choices:

```text
right_count = 3 - 1 = 2
```

The endpoints may be index `1` or index `2`.

The stack is empty, so use left wall `-1`:

```text
left_count = 1 - (-1) = 2
```

The starts may be index `0` or index `1`.

Contribution:

```text
1 * 2 * 2 = 4
total_sum = 5 + 4 = 9
```

`1` owns four subarrays:

```text
[1]
[3, 1]
[1, 2]
[3, 1, 2]
```

The dummy `(3, 0)` is pushed. Its value is zero, so it contributes nothing.

Final answer:

```text
9
```

All original subarrays confirm the result:

```text
[3]       -> 3
[1]       -> 1
[2]       -> 2
[3, 1]    -> 1
[1, 2]    -> 1
[3, 1, 2] -> 1
                --
                 9
```

## Alternative: grouped running ending sums

The second saved solution groups all subarrays ending at the current index by their minimum. Its stack entries are `(minimum, count)` rather than `(index, value)`.

When a smaller number arrives, it takes ownership of groups with greater or equal minimums. `ending_sum` tracks the sum of minimums for all subarrays ending at the current index.

See `solution-running-sum.py` for that implementation.

## Complexity

- Time: `O(n)`. Each element enters the stack once and leaves it at most once.
- Space: `O(n)` for the monotonic stack and the extended array.

## Memory rule

> A number contributes its value multiplied by its left choices and right choices. The increasing stack waits until a smaller number reveals each value's right wall.
