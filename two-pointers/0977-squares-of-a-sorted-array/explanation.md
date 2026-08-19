# 977. Squares of a Sorted Array

## Problem in simple words

Square every value in a sorted integer array and return the squares in non-decreasing order.

```text
nums = [-4, -1, 0, 3, 10]
result = [0, 1, 9, 16, 100]
```

## Why squaring breaks the original order

Negative numbers reverse their size relationship after squaring:

```text
-4 < -1
16 > 1 after squaring
```

Therefore, simply squaring each value produces:

```text
[16, 1, 0, 9, 100]
```

The array must still be reordered.

## Version 1: square and sort

The simplest approach is to square every element and then use the language's sorting algorithm.

```python
class Solution(object):
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

        nums.sort()
        return nums
```

### How it works

```text
Original:       [-4, -1, 0, 3, 10]
After squaring: [16, 1, 0, 9, 100]
After sorting:  [0, 1, 9, 16, 100]
```

### Complexity

- Squaring: `O(n)`
- Sorting: `O(n log n)`
- Overall time: `O(n log n)`
- Extra space: depends on the sorting implementation

This version is easy to write and understand, but it does not take full advantage of the input already being sorted.

## Version 2: two pointers

In a sorted array, the value with the largest absolute value must be at one of the ends:

```text
nums = [-4, -1, 0, 3, 10]
         ↑              ↑
       left           right
```

The largest square therefore comes from either `nums[left]` or `nums[right]`. Compare their absolute values, put the larger square into the last empty result position, and move that pointer inward.

```python
class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1

        for write in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[write] = nums[left] ** 2
                left += 1
            else:
                result[write] = nums[right] ** 2
                right -= 1

        return result
```

## Why fill the result backward?

The pointers reveal the largest remaining square first. The result must be sorted from smallest to largest, so place each discovered square at the last available index:

```text
write = n - 1, n - 2, ..., 0
```

## Two-pointer dry run

For `nums = [-4, -1, 0, 3, 10]`:

| Left square | Right square | Larger value placed | Write index |
|---:|---:|---:|---:|
| 16 | 100 | 100 | 4 |
| 16 | 9 | 16 | 3 |
| 1 | 9 | 9 | 2 |
| 1 | 0 | 1 | 1 |
| 0 | 0 | 0 | 0 |

```text
result = [0, 1, 9, 16, 100]
```

## Pointer movement

- If the left square is larger, store it and move `left` right.
- Otherwise, store the right square and move `right` left.
- Move `write` left after every placement.

Equal squares can be taken from either side. The implementation takes the right square in the `else` branch.

## Complexity of the two-pointer version

- Time: `O(n)`
- Extra space: `O(n)` for the required result array

## Comparing both versions

| Approach | Time | Main advantage |
|---|---:|---|
| Square, then sort | `O(n log n)` | Short and straightforward |
| Two pointers | `O(n)` | Uses the sorted input optimally |

## Edge cases

- All values are negative.
- All values are non-negative.
- Both ends produce equal squares.
- The input contains one element.

## Common mistakes

- Assuming squares remain sorted after transforming negative values.
- Filling the two-pointer result from the beginning even though the largest square is found first.
- Comparing the raw end values instead of their squares or absolute values.

## What I learned

When a sorted array is transformed by squaring, its largest results come from the ends. Compare both ends and build the result backward.
