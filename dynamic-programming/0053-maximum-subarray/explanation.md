# 53. Maximum Subarray

## Problem in simple words

Find the largest sum that can be produced by a contiguous, non-empty section of the array.

```text
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Best subarray: [4, -1, 2, 1]
Sum: 6
```

## Intuition

At each number, there are only two useful choices:

1. Extend the subarray ending at the previous position.
2. Discard the previous subarray and start a new one at the current number.

If the previous running sum hurts the current number, starting over is better. This is Kadane's algorithm.

## State and transition

`current_sum` is the largest sum of a subarray that must end at the current position:

```python
current_sum = max(num, current_sum + num)
```

`max_sum` is the best sum found anywhere so far:

```python
max_sum = max(max_sum, current_sum)
```

## Step-by-step approach

1. Initialize both sums with the first number.
2. Scan the remaining numbers from left to right.
3. For each number, choose between starting over and extending the previous subarray.
4. Update the overall maximum.
5. Return the overall maximum.

## Dry run

For `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`:

| Number | Best sum ending here | Best overall |
|---:|---:|---:|
| -2 | -2 | -2 |
| 1 | 1 | 1 |
| -3 | -2 | 1 |
| 4 | 4 | 4 |
| -1 | 3 | 4 |
| 2 | 5 | 5 |
| 1 | 6 | 6 |
| -5 | 1 | 6 |
| 4 | 5 | 6 |

The maximum subarray sum is `6`.

## Implementation

```python
class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
```

## Why initialize with the first number?

The subarray must be non-empty. Initializing to `0` would incorrectly return `0` for an all-negative array such as `[-3, -1, -2]`, whose correct answer is `-1`.

## Complexity

- Time: `O(n)`
- Extra space: `O(1)`

## Edge cases

- One element returns that element.
- An all-negative array returns its largest single value.
- An all-positive array returns the sum of the entire array.

## Common mistake

Do not reset a negative running sum to `0` when the problem requires a non-empty subarray unless the all-negative case is handled separately.

## What I learned

When a problem asks for the best contiguous segment, consider tracking the best segment that must end at each current position.
