# 209. Minimum Size Subarray Sum

## Problem in simple words

Find the shortest contiguous, non-empty section of `nums` whose sum is at least `target`. Return `0` if no such section exists.

All values are positive, which makes a sliding window possible.

## Elastic-rubber-band analogy

Imagine the array is a row of numbered blocks and an elastic rubber band surrounds a connected group of them.

Your goal is to make the rubber band cover blocks whose total is at least `target`, while keeping the band as short as possible.

### Stretch to the right

The `right` pointer stretches the rubber band over one additional block:

```python
current_sum += nums[right]
```

Keep stretching until the covered values reach the target.

### Shrink from the left

Once the sum is valid, pull the left edge inward:

```python
current_sum -= nums[left]
left += 1
```

Continue shrinking while the sum remains at least the target. This tests every shorter valid window ending at the current `right` position.

### Record the best measurement

Before removing the leftmost block, measure the valid window:

```python
current_length = right - left + 1
min_length = min(min_length, current_length)
```

## Why does `right - left + 1` give the length?

Both boundary indexes are included.

For a window from index `1` through index `4`:

```text
indexes: 1, 2, 3, 4
```

Subtracting gives the number of gaps:

```text
4 - 1 = 3
```

Adding one includes the starting element:

```text
4 - 1 + 1 = 4 elements
```

> Length memory rule: inclusive endpoints require `+1`.

## Why initialize `min_length` to infinity?

```python
min_length = float("inf")
```

Every real window length is smaller than infinity, so the first valid window automatically becomes the current best.

If infinity remains unchanged, no window ever reached the target:

```python
return min_length if min_length != float("inf") else 0
```

## Why positive numbers matter

Because every number is positive:

- Moving `right` forward can only increase the sum.
- Moving `left` forward can only decrease the sum.

That predictable direction makes it safe to expand when the sum is too small and shrink when it is large enough.

With negative numbers, removing a value could increase the sum and adding a value could decrease it, so this sliding-window rule would not remain valid.

## Implementation with comments

```python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        # Start with infinity because we want to find a smaller valid length.
        min_length = float("inf")
        current_sum = 0
        left = 0

        # Expand the right side of the window one element at a time.
        for right in range(len(nums)):
            current_sum += nums[right]

            # While the window is valid, record its length and shrink it from
            # the left to search for a shorter valid window.
            while current_sum >= target:
                current_length = right - left + 1
                min_length = min(min_length, current_length)

                # Remove the leftmost value before advancing the left pointer.
                current_sum -= nums[left]
                left += 1

        # Infinity means no window ever reached the target.
        return min_length if min_length != float("inf") else 0
```

## Complete dry run

```python
target = 7
nums = [2, 3, 1, 2, 4, 3]
```

Initialize:

```text
min_length = infinity
current_sum = 0
left = 0
```

### `right = 0`, value `2`

```text
current_sum = 0 + 2 = 2
2 < 7 → do not shrink
```

Window:

```text
[2]
```

### `right = 1`, value `3`

```text
current_sum = 2 + 3 = 5
5 < 7 → do not shrink
```

Window:

```text
[2, 3]
```

### `right = 2`, value `1`

```text
current_sum = 5 + 1 = 6
6 < 7 → do not shrink
```

Window:

```text
[2, 3, 1]
```

### `right = 3`, value `2`

```text
current_sum = 6 + 2 = 8
8 >= 7 → valid window
```

Measure:

```text
current_length = 3 - 0 + 1 = 4
min_length = min(infinity, 4) = 4
```

Window:

```text
[2, 3, 1, 2]
```

Shrink from the left:

```text
current_sum = 8 - nums[0]
            = 8 - 2
            = 6
left = 1
```

Now `6 < 7`, so stop shrinking.

### `right = 4`, value `4`

```text
current_sum = 6 + 4 = 10
10 >= 7 → valid
```

Current window:

```text
[3, 1, 2, 4]
```

Measure:

```text
current_length = 4 - 1 + 1 = 4
min_length = min(4, 4) = 4
```

Shrink by removing `nums[1] = 3`:

```text
current_sum = 10 - 3 = 7
left = 2
```

The sum is still valid, so the `while` loop continues.

Current window:

```text
[1, 2, 4]
```

Measure again:

```text
current_length = 4 - 2 + 1 = 3
min_length = min(4, 3) = 3
```

Shrink by removing `nums[2] = 1`:

```text
current_sum = 7 - 1 = 6
left = 3
```

Now `6 < 7`, so stop shrinking.

### `right = 5`, value `3`

```text
current_sum = 6 + 3 = 9
9 >= 7 → valid
```

Current window:

```text
[2, 4, 3]
```

Measure:

```text
current_length = 5 - 3 + 1 = 3
min_length = min(3, 3) = 3
```

Shrink by removing `nums[3] = 2`:

```text
current_sum = 9 - 2 = 7
left = 4
```

Still valid. Current window:

```text
[4, 3]
```

Measure again:

```text
current_length = 5 - 4 + 1 = 2
min_length = min(3, 2) = 2
```

Shrink by removing `nums[4] = 4`:

```text
current_sum = 7 - 4 = 3
left = 5
```

Now `3 < 7`, so stop.

### Return

```text
min_length = 2
```

The shortest valid subarray is `[4, 3]`.

## Why the nested loops are still `O(n)`

Although a `while` loop appears inside a `for` loop, neither pointer moves backward:

- `right` visits each index once.
- `left` visits each index at most once.
- Each value is added to `current_sum` once.
- Each value is subtracted at most once.

There are at most approximately `2n` pointer movements, so the total time is `O(n)`, not `O(n²)`.

## Complexity

- Time: `O(n)`
- Extra space: `O(1)`

## Edge cases

- One value alone reaches the target, so the answer is `1`.
- The whole array is required.
- The total array sum is below the target, so return `0`.
- Multiple valid windows exist; retain the shortest one.

## Common mistakes

- Using `if` instead of `while` and shrinking only once per right endpoint.
- Forgetting `+1` in the inclusive window length.
- Moving `left` without subtracting the value leaving the window.
- Returning infinity when no valid window exists.
- Applying this exact strategy to arrays containing negative values.

## What I learned

Stretch the rubber band until its sum is valid, then pull its left edge inward as far as possible while measuring every valid size.
