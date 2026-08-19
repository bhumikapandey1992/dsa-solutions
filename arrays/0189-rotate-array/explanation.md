# 189. Rotate Array

## Problem in simple words

Move every element in `nums` `k` positions to the right. Elements that move beyond the end wrap around to the beginning, and the modification must happen in place.

```text
nums = [1, 2, 3, 4, 5, 6, 7], k = 3
result = [5, 6, 7, 1, 2, 3, 4]
```

## Normalize `k` first

Think of rotating an array like moving around a clock or spinning a wheel. Moving a clock hand forward by exactly 12 hours brings it back to its starting position. Moving it 13 hours has the same final effect as moving it only 1 hour.

An array behaves the same way. One complete cycle contains `n` rotations and returns every element to its original position. Therefore, only the rotations left over after removing complete cycles matter.

### Watch a three-element array complete a cycle

```text
Start:          [A, B, C]
Rotate 1 time:  [C, A, B]
Rotate 2 times: [B, C, A]
Rotate 3 times: [A, B, C]  ← back to the beginning
Rotate 4 times: [C, A, B]  ← same result as 1 rotation
```

Because the length is `3`, every group of three rotations does nothing to the final arrangement. Four rotations consist of one complete cycle plus one useful rotation.

### The modulo operator removes complete cycles

Modulo `%` gives the remainder after division:

```python
k %= len(nums)
```

It strips away all complete cycles and keeps only the number of rotations that can change the final arrangement.

```text
k = 4, n = 3
4 % 3 = 1
4 rotations are equivalent to 1 rotation.

k = 10, n = 7
10 % 7 = 3
10 rotations are equivalent to 3 rotations.

k = 7000, n = 7
7000 % 7 = 0
7000 rotations are equivalent to no rotation.
```

### Why normalization also prevents bugs

The second reversal uses this range:

```python
reverse(0, k - 1)
```

If `n = 7` and an unnormalized `k = 10`, the code would call `reverse(0, 9)`. Indexes `7`, `8`, and `9` do not exist, so accessing them would raise an `IndexError`.

After normalization:

```text
k = 10 % 7 = 3
reverse(0, k - 1) becomes reverse(0, 2)
```

That range is valid and represents the only three rotations that actually matter.

### Modulo memory rule

> A full trip around the array changes nothing; modulo keeps only the unfinished part of the trip.

## Intuition: split the final result into two groups

After rotating right by `k`, the final array contains:

```text
[last k elements] + [first n - k elements]
```

For the example:

```text
original: [1, 2, 3, 4 | 5, 6, 7]
result:   [5, 6, 7 | 1, 2, 3, 4]
```

We could build that result with a new array, but the problem asks for an in-place solution. Three reversals rearrange the same two groups without extra storage.

## Three-reversal strategy

### 1. Reverse the entire array

```text
[1, 2, 3, 4, 5, 6, 7]
             ↓
[7, 6, 5, 4, 3, 2, 1]
```

The elements that belong at the front are now there, but their internal order is backward.

### 2. Reverse the first `k` elements

```text
[7, 6, 5 | 4, 3, 2, 1]
     ↓
[5, 6, 7 | 4, 3, 2, 1]
```

The rotated front group is now correct.

### 3. Reverse the remaining `n - k` elements

```text
[5, 6, 7 | 4, 3, 2, 1]
                 ↓
[5, 6, 7 | 1, 2, 3, 4]
```

Both groups now have the correct order.

## Pointer ranges

```python
reverse(0, n - 1)  # Entire array
reverse(0, k - 1)  # First k positions
reverse(k, n - 1)  # Remaining positions
```

The ranges are inclusive, so the last index of a group is one less than its length.

## Implementation

```python
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
```

## Why the helper works

The `reverse` helper swaps the outside elements, moves both pointers inward, and stops when they meet or cross.

```text
[1, 2, 3, 4]
 ↑        ↑      swap
    ↑  ↑         swap
[4, 3, 2, 1]
```

## Complexity

- Time: `O(n)`
- Extra space: `O(1)`

## Edge cases

- `k` is larger than the array length: reduce it with modulo.
- `k` is a multiple of the length: the final arrangement is unchanged.
- The array contains one element: every reversal is harmless.

## Common mistakes

- Forgetting `k %= n`, which can produce invalid range boundaries.
- Reversing the groups before reversing the entire array.
- Returning a new array instead of modifying `nums` in place.

## What I learned

When rotation divides an array into two groups, reversing the whole array and then repairing each group's internal order can perform the rearrangement in place.
