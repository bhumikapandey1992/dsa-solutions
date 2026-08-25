# 918. Maximum Sum Circular Subarray

## Problem in simple words

Find the largest sum of a non-empty contiguous subarray. The array is circular, so a subarray may continue from the last element back to the first.

The answer has one of two shapes:

1. It stays inside the array without wrapping.
2. It uses a suffix from the end and a prefix from the beginning.

## Analogy: a circular necklace

Imagine the array as a necklace whose last bead connects to its first bead.

For a non-wrapping answer, choose the best ordinary consecutive section. Standard Kadane's algorithm finds it.

For a wrapping answer, it is easier to think backward:

> Keep the whole necklace, then cut out its worst consecutive section.

If the entire necklace has sum `total_sum` and its worst section has sum `global_min`, the beads left around the circular connection have sum:

```text
circular_max = total_sum - global_min
```

For example:

```text
[5, -3, 5]
```

The total is `7`. Cut out the worst section `[-3]`:

```text
7 - (-3) = 10
```

The remaining two end beads connect through the circle:

```text
[5] + [5] = 10
```

## Why run Kadane's algorithm twice?

### Maximum Kadane

```python
current_max = max(num, current_max + num)
global_max = max(global_max, current_max)
```

At each number, either:

- start a new subarray at this number; or
- extend the best subarray ending at the previous position.

This finds the best normal, non-wrapping subarray.

### Minimum Kadane

```python
current_min = min(num, current_min + num)
global_min = min(global_min, current_min)
```

This makes the same decision in the opposite direction. It finds the worst consecutive section to cut out of the necklace.

## The two candidates

```python
normal_max = global_max
circular_max = total_sum - global_min
return max(normal_max, circular_max)
```

We must compare both because wrapping is allowed but not required.

For `[1, -2, 3, -2]`, the best answer is the ordinary subarray `[3]`. Cutting out the minimum section does not produce something better.

## Commented solution

```python
class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total_sum = nums[0]

        current_max = nums[0]
        global_max = nums[0]

        current_min = nums[0]
        global_min = nums[0]

        for num in nums[1:]:
            total_sum += num

            current_max = max(num, current_max + num)
            global_max = max(global_max, current_max)

            current_min = min(num, current_min + num)
            global_min = min(global_min, current_min)

        if global_max < 0:
            return global_max

        normal_max = global_max
        circular_max = total_sum - global_min

        return max(normal_max, circular_max)
```

## Complete dry run

```python
nums = [5, -3, 5]
```

Initialize from the first value:

```text
total_sum = 5

current_max = 5
global_max = 5

current_min = 5
global_min = 5
```

### Process `-3`

Add it to the whole-array total:

```text
total_sum = 5 + (-3) = 2
```

Maximum Kadane:

```text
current_max = max(-3, 5 + (-3))
            = max(-3, 2)
            = 2

global_max = max(5, 2) = 5
```

The best subarray ending here is `[5, -3]`, but the all-time best remains `[5]`.

Minimum Kadane:

```text
current_min = min(-3, 5 + (-3))
            = min(-3, 2)
            = -3

global_min = min(5, -3) = -3
```

The worst section found so far is `[-3]`.

### Process `5`

Update the total:

```text
total_sum = 2 + 5 = 7
```

Maximum Kadane:

```text
current_max = max(5, 2 + 5)
            = max(5, 7)
            = 7

global_max = max(5, 7) = 7
```

The best normal subarray is the entire array, with sum `7`.

Minimum Kadane:

```text
current_min = min(5, -3 + 5)
            = min(5, 2)
            = 2

global_min = min(-3, 2) = -3
```

The worst section remains `[-3]`.

### Compare the final candidates

Normal candidate:

```text
normal_max = global_max = 7
```

Circular candidate—cut the worst section out of the necklace:

```text
circular_max = total_sum - global_min
             = 7 - (-3)
             = 10
```

Choose the larger candidate:

```text
max(7, 10) = 10
```

The answer uses the last `5`, wraps around, and includes the first `5`.

## Critical edge case: every number is negative

Consider:

```python
nums = [-3, -2, -3]
```

Here the minimum subarray is the entire array:

```text
total_sum = -8
global_min = -8
```

The circular formula would give:

```text
total_sum - global_min = -8 - (-8) = 0
```

But this removes the entire necklace and keeps no beads. The problem requires a non-empty subarray, so `0` is invalid.

The best legitimate answer is the largest single element, `-2`. Maximum Kadane already found it:

```python
if global_max < 0:
    return global_max
```

## Why checking `global_max < 0` works

If `global_max` is negative, every number is negative. If even one number were zero or positive, the maximum subarray sum would be at least zero.

Therefore, this condition precisely identifies the case where subtracting the minimum would remove the whole array.

## Complexity

- Time: `O(n)` because the array is scanned once.
- Extra space: `O(1)` because only running sums are stored.

## Memory rule

> The answer is either the best ordinary section, or the whole circular necklace after cutting out its worst section. If every bead is negative, keep the least-negative bead instead of cutting everything away.
