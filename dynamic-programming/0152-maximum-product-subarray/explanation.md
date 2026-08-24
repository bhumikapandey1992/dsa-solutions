# 152. Maximum Product Subarray

## Problem in simple words

Find the largest product produced by a contiguous, non-empty section of the array.

This resembles Maximum Subarray, but multiplication introduces two complications:

- A negative number reverses which product is largest and smallest.
- Zero breaks the existing product chain and allows a new chain to begin.

## Three tracking values

```text
current_max = largest product of a subarray that must end here
current_min = smallest product of a subarray that must end here
global_max  = largest product found anywhere so far
```

`current_max` and `current_min` describe subarrays ending at the current position. `global_max` remembers the answer even after the scan moves elsewhere.

## Why keep the smallest product?

A negative result may become extremely valuable after another negative number:

```text
-6 × -4 = 24
```

Think of the two running products as a mountain:

```text
current_max → positive peak
current_min → negative valley
```

A negative multiplier flips the mountain. The valley may become the next peak.

## Why do maximum and minimum swap roles?

Suppose:

```text
current_max = 10
current_min = -5
num = -2
```

Multiplying both by `-2` produces:

```text
old maximum:  10 × -2 = -20
old minimum:  -5 × -2 = 10
```

The old maximum creates the new minimum, while the old minimum creates the new maximum.

Mathematically:

```text
current_min <= current_max
```

Multiplying the inequality by a negative reverses it:

```text
current_min × num >= current_max × num
```

The swap makes each update use the correct old value:

```python
if num < 0:
    current_max, current_min = current_min, current_max
```

## What if the old minimum is positive?

The swap still works. Suppose:

```text
current_max = 10
current_min = 2
num = -3
```

Both stored products are positive, but negative multiplication still reverses their order:

```text
10 × -3 = -30
2 × -3  = -6

-6 > -30
```

The old minimum still produces the larger extended product.

After the blind swap:

```text
current_max = 2
current_min = 10
```

The update guardrails choose the correct final values:

```python
current_max = max(-3, 2 * -3)   # max(-3, -6) = -3
current_min = min(-3, 10 * -3)  # min(-3, -30) = -30
```

Final state:

```text
current_max = -3
current_min = -30
```

We do not need to check whether the old minimum is negative. Multiplication by a negative always reverses the order, and the following `max()` and `min()` calls decide whether extending either chain is useful.

## Why compare with `num` itself?

At every position, there are two choices:

1. Start a new subarray containing only `num`.
2. Extend a product ending at the previous position.

```python
current_max = max(num, current_max * num)
current_min = min(num, current_min * num)
```

For example:

```text
previous current_max = -2
num = 4

extend:    -2 × 4 = -8
start new: 4
```

`max(4, -8)` chooses `4`, abandoning the harmful previous chain.

## Why zero works automatically

Suppose:

```text
current_max = 12
current_min = -6
num = 0
```

Then:

```text
current_max = max(0, 12 × 0) = 0
current_min = min(0, -6 × 0) = 0
```

Zero resets both chains. The next nonzero value can start a fresh subarray.

## Implementation with comments

```python
class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0

        # Initialize all tracking values with the first number.
        global_max = nums[0]

        # Largest product of a subarray that must end at the current position.
        current_max = nums[0]

        # Smallest product of a subarray that must end at the current position.
        # A later negative number can turn this negative valley into a peak.
        current_min = nums[0]

        # Process the remaining numbers.
        for i in range(1, len(nums)):
            num = nums[i]

            # Multiplication by a negative reverses numeric order. The previous
            # minimum can become the new maximum, and vice versa.
            if num < 0:
                current_max, current_min = current_min, current_max

            # Either start a new subarray at num or extend the best previous
            # product ending immediately before this position.
            current_max = max(num, current_max * num)

            # Preserve the smallest product because another negative number
            # could turn it into a large positive product later.
            current_min = min(num, current_min * num)

            # Record the best product found anywhere in the array.
            global_max = max(global_max, current_max)

        return global_max
```

## Line-by-line dry run: `[2, 3, -2, 4]`

### Initialization

```text
global_max = 2
current_max = 2
current_min = 2
```

### Process `3`

`3` is positive, so do not swap.

```text
current_max = max(3, 2 × 3) = 6
current_min = min(3, 2 × 3) = 3
global_max  = max(2, 6)     = 6
```

State:

```text
current_max = 6
current_min = 3
global_max = 6
```

### Process `-2`

`-2` is negative, so swap first:

```text
before: current_max = 6, current_min = 3
after:  current_max = 3, current_min = 6
```

Now update:

```text
current_max = max(-2, 3 × -2) = -2
current_min = min(-2, 6 × -2) = -12
global_max  = max(6, -2)      = 6
```

The algorithm stores `-12` because another negative could turn it into a large positive value.

### Process `4`

`4` is positive, so do not swap:

```text
current_max = max(4, -2 × 4)  = 4
current_min = min(4, -12 × 4) = -48
global_max  = max(6, 4)       = 6
```

Starting fresh at `4` is better than extending the negative maximum chain.

### Return

```text
return 6
```

The winning subarray is `[2, 3]`.

## Dry run proving why `current_min` matters

For:

```python
nums = [-2, 3, -4]
```

After processing `-2` and `3`:

```text
current_max = 3
current_min = -6
global_max = 3
```

Now process `-4`. Swap first:

```text
current_max = -6
current_min = 3
```

Then:

```text
current_max = max(-4, -6 × -4) = 24
current_min = min(-4, 3 × -4)  = -12
global_max  = max(3, 24)       = 24
```

The stored negative valley produces the winning positive peak:

```text
[-2, 3, -4] → 24
```

Without `current_min`, the algorithm would miss this result.

## Complexity

- Time: `O(n)`
- Extra space: `O(1)`

## Edge cases

- A single negative value must be returned instead of zero.
- Zero resets the running products.
- Two negative numbers may create the maximum positive product.
- An odd number of negative values may require excluding one side of a segment.
- The best subarray may begin after a zero.

## Common mistakes

- Tracking only `current_max` and losing a useful negative product.
- Updating `current_max` before saving the old value needed for `current_min`.
- Forgetting to swap when the current number is negative.
- Initializing with zero and incorrectly allowing an empty subarray.
- Returning the final `current_max` instead of the best `global_max` seen anywhere.

## What I learned

Keep both the positive peak and negative valley. A negative number flips their roles, and `max`/`min` decide whether to extend the chain or start over.
