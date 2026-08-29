# 15. 3Sum

## Problem in simple words

Find every unique triplet of values whose sum is zero. The three values must come from three different indices, and duplicate triplets are not allowed.

## Analogy: balancing a scale

Place one fixed number on a scale:

```text
fixed + left + right = 0
```

The two moving values must balance it:

```text
left + right = -fixed
```

After sorting, moving `left` right selects a larger value, while moving `right` left selects a smaller value. This lets us adjust the total deliberately rather than trying every possible triple.

## The pointer roles

```python
for i in range(len(nums)):
    left = i + 1
    right = len(nums) - 1
```

`i` is an index that moves through the array in the outer loop. During one iteration, `nums[i]` is the fixed first value.

`left` does not start at zero. It starts immediately after the fixed index:

```text
i < left < right
```

This guarantees three different indices and avoids revisiting combinations from the earlier part of the sorted array.

For each new `i`:

- `left` restarts at `i + 1`;
- `right` restarts at the final index;
- `i` stays fixed while the other two pointers move toward each other.

## Why sorting is essential

Sorting provides two abilities:

1. Pointer movement changes the sum predictably.
2. Equal values become adjacent, making duplicates easy to skip.

Without sorting, moving a pointer right would not guarantee a larger value.

## Why a positive fixed value lets us stop

```python
if nums[i] > 0:
    break
```

This is safe because the array was sorted first. Every available value after `i` is at least `nums[i]`.

If `nums[i]` is positive, then `nums[left]` and `nums[right]` are also positive:

```text
positive + positive + positive > 0
```

No current or later fixed value can create zero, so we stop the entire outer loop with `break`.

The condition must be `> 0`, not `>= 0`, because this is valid:

```text
[0, 0, 0]
```

This optimization would not be safe before sorting. For unsorted `[2,-3,1]`, the first value is positive but all three values sum to zero.

## Skipping a duplicate fixed value

```python
if i > 0 and nums[i] == nums[i - 1]:
    continue
```

After the first occurrence of a value has searched every pair to its right, fixing the same value again would recreate triplets already found.

`continue` skips only that duplicate iteration and proceeds to the next possible fixed value.

## Moving the two pointers

```python
total = nums[i] + nums[left] + nums[right]
```

If the total is too small:

```python
if total < 0:
    left += 1
```

Move `left` toward a larger value.

If the total is too large:

```python
elif total > 0:
    right -= 1
```

Move `right` toward a smaller value.

If the total is zero, save the triplet and move both pointers to search for a different pair.

## Skipping duplicate pointer values

The saved solution skips duplicates before the final pointer movement:

```python
while left < right and nums[left] == nums[left + 1]:
    left += 1
while left < right and nums[right] == nums[right - 1]:
    right -= 1

left += 1
right -= 1
```

For a run of equal values, the loops move to the last equal copy on the left and the first equal copy on the right. The final increments then move beyond those duplicate groups.

This prevents the same value triplet from being appended repeatedly.

## Commented implementation

```python
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[right] + nums[left]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result
```

## Complete dry run

```python
nums = [-1, 0, 1, 2, -1, -4]
```

Sort first:

```text
values: [-4, -1, -1, 0, 1, 2]
indices:   0   1   2  3  4  5
```

### Fix index `0`, value `-4`

```text
i = 0
left = 1  -> -1
right = 5 -> 2
```

```text
-4 + -1 + 2 = -3
```

The sum is too small, so move `left` right. The next value is another `-1`, then `0`, then `1`; every total remains negative:

```text
-4 + -1 + 2 = -3
-4 +  0 + 2 = -2
-4 +  1 + 2 = -1
```

The pointers meet. No zero-sum triplet starts with `-4`.

### Fix index `1`, value `-1`

```text
i = 1
left = 2  -> -1
right = 5 -> 2
```

```text
-1 + -1 + 2 = 0
```

Record:

```text
[-1, -1, 2]
```

There are no adjacent duplicates to skip at these pointer positions. Move both:

```text
left = 3  -> 0
right = 4 -> 1
```

Now:

```text
-1 + 0 + 1 = 0
```

Record:

```text
[-1, 0, 1]
```

Move both pointers. They meet, so this inner search ends.

### Fix index `2`, value `-1`

This equals the previous fixed value:

```text
nums[2] == nums[1]
```

Skip it so the same triplets are not generated again.

### Fix index `3`, value `0`

```text
left = 4  -> 1
right = 5 -> 2
```

```text
0 + 1 + 2 = 3
```

The sum is too large, so move `right` left. The pointers meet, and no triplet is found.

### Reach a positive fixed value

The next fixed value is `1`. Because the array is sorted, every available value after it is also positive. Stop the loop.

Final result:

```python
[
    [-1, -1, 2],
    [-1, 0, 1]
]
```

## About `range(len(nums))`

The saved code is correct with:

```python
for i in range(len(nums)):
```

Near the end, `left >= right`, so the inner loop simply does not execute. It could be slightly tightened to:

```python
for i in range(len(nums) - 2):
```

because a triplet requires two values after `i`, but this does not change the result or overall complexity.

## Complexity

- Sorting: `O(n log n)`.
- Two-pointer searches: `O(n²)` overall.
- Total time: `O(n²)`.
- Extra algorithmic space: `O(1)` excluding sorting internals and the output.

## Memory rule

> Sort the array, fix one value, start `left` immediately after it, and squeeze `left` and `right` toward a total of zero. Skip repeated values at every role.
