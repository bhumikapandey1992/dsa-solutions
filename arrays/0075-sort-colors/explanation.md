# 75. Sort Colors

## Problem in simple words

Sort an array containing only `0`, `1`, and `2` in place:

```text
0 = red
1 = white
2 = blue
```

For example:

```text
nums = [2, 0, 2, 1, 1, 0]
result = [0, 0, 1, 1, 2, 2]
```

The method must modify `nums` itself and does not return a new array.

## Counting approach

Because there are exactly three possible values, use a three-entry list to count them:

```python
counts = [0, 0, 0]
```

Each index represents a color:

```text
counts[0] = number of zeros
counts[1] = number of ones
counts[2] = number of twos
```

## Why `counts[color]` works

The input values are already `0`, `1`, or `2`, so each value can be used directly as an index:

```python
for color in nums:
    counts[color] += 1
```

For `nums = [2, 0, 2, 1, 1, 0]`:

| Color read | Counter updated | Counts afterward |
|---:|---|---|
| 2 | `counts[2]` | `[0, 0, 1]` |
| 0 | `counts[0]` | `[1, 0, 1]` |
| 2 | `counts[2]` | `[1, 0, 2]` |
| 1 | `counts[1]` | `[1, 1, 2]` |
| 1 | `counts[1]` | `[1, 2, 2]` |
| 0 | `counts[0]` | `[2, 2, 2]` |

The final counts mean there are two values of each color.

## Unpacking the counts

```python
red, white, blue = counts
```

For the example:

```text
red   = 2
white = 2
blue  = 2
```

These names represent quantities, not array values.

## Rebuilding `nums` with slices

### Fill the first `red` positions with zeros

```python
nums[:red] = [0] * red
```

If `red = 2`, the slice is `nums[:2]`, which covers indexes `0` and `1`:

```text
[0, 0, _, _, _, _]
```

### Fill the next `white` positions with ones

```python
nums[red:red + white] = [1] * white
```

If `red = 2` and `white = 2`, the slice is `nums[2:4]`, covering indexes `2` and `3`:

```text
[0, 0, 1, 1, _, _]
```

### Fill the remaining positions with twos

```python
nums[red + white:] = [2] * blue
```

`red + white = 4`, so `nums[4:]` covers the remaining positions:

```text
[0, 0, 1, 1, 2, 2]
```

## Slice boundary memory rule

```text
zeros: [0, red)
ones:  [red, red + white)
twos:  [red + white, end)
```

Python includes the starting slice index and excludes the ending index.

## Implementation

```python
class Solution(object):
    def sortColors(self, nums):
        counts = [0, 0, 0]

        for color in nums:
            counts[color] += 1

        red, white, blue = counts
        nums[:red] = [0] * red
        nums[red:red + white] = [1] * white
        nums[red + white:] = [2] * blue
```

## Why is there no return statement?

LeetCode asks this method to modify `nums` in place. The caller sees the changes made to the original list, so returning it is unnecessary.

## Complexity

- Counting pass: `O(n)`
- Rebuilding the array: `O(n)`
- Total time: `O(n)`
- Counter space: `O(1)` because `counts` always has three entries

The slice expressions create temporary lists during assignment. The Dutch National Flag algorithm is the stricter one-pass solution with constant auxiliary storage throughout.

## Edge cases

- All elements have the same color.
- One or more colors are missing.
- The array contains one element.
- The array is already sorted.

## Common mistakes

- Forgetting that the color value itself is the counter index.
- Miscalculating the second boundary as only `white` instead of `red + white`.
- Returning a new list instead of modifying `nums`.
- Calling general-purpose sorting when the goal is to practice the problem's intended patterns.

## What I learned

When values come from a tiny fixed range, count each value and overwrite the array in contiguous sections using cumulative boundaries.
