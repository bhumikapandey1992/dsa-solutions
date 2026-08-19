# 167. Two Sum II - Input Array Is Sorted

## Problem in simple words

Find two different values in a sorted array whose sum equals `target`. Return their positions using 1-based indexing.

```text
numbers = [2, 7, 11, 15], target = 9

2 + 7 = 9
answer = [1, 2]
```

## Why sorting matters

The sorted order tells us exactly how to adjust an incorrect sum:

- Moving the left pointer right chooses a value that is equal or larger, so the sum increases.
- Moving the right pointer left chooses a value that is equal or smaller, so the sum decreases.

This lets us eliminate impossible pairs without testing every combination.

## Pointer setup

```python
left = 0
right = len(numbers) - 1
```

Start with the smallest and largest values in the array.

## Movement logic

Calculate:

```python
current_sum = numbers[left] + numbers[right]
```

Then make one of three decisions:

### The sum equals the target

Return both positions. Add `1` because the problem requires 1-indexed positions:

```python
return [left + 1, right + 1]
```

### The sum is too small

The current left value is the smallest remaining option. Pairing it with any value left of `right` would make the sum even smaller, so it cannot be part of the answer. Move `left` right to choose a larger value:

```python
left += 1
```

### The sum is too large

The current right value is the largest remaining option. Pairing it with any value right of `left` would keep the sum too large, so it cannot be part of the answer. Move `right` left to choose a smaller value:

```python
right -= 1
```

## Dry run

```text
numbers = [2, 7, 11, 15], target = 9
```

| Left value | Right value | Sum | Decision |
|---:|---:|---:|---|
| 2 | 15 | 17 | Too large: move `right` left |
| 2 | 11 | 13 | Too large: move `right` left |
| 2 | 7 | 9 | Match: return `[1, 2]` |

## Visual memory model

```text
Too small  → move LEFT  →
Too large  ← move RIGHT
```

The pointers squeeze inward until they find the target sum.

## Implementation

```python
class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]

            if current_sum < target:
                left += 1
            else:
                right -= 1
```

## Why `left < right`?

The two numbers must come from different positions. When the pointers meet, only one element remains, so it cannot form a valid pair with itself.

## Complexity

- Time: `O(n)`
- Extra space: `O(1)`

## Edge cases

- Negative numbers: sorted-order pointer movement still works.
- Duplicate values: two different positions can contain the same value.
- The answer can use the first or last element.

## Common mistakes

- Returning zero-based indexes instead of adding `1`.
- Moving the wrong pointer when the sum is too small or too large.
- Using a hash map and missing the constant-space benefit of the sorted input.

## What I learned

For a sorted array, comparing the smallest and largest remaining values reveals which side can safely be discarded.
