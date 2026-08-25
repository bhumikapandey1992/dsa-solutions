# 713. Subarray Product Less Than K

## Problem in simple words

Count every contiguous subarray whose product is strictly less than `k`.

All values in `nums` are positive, so a variable-size sliding window works.

## Elastic-window intuition

Imagine stretching an elastic band over a row of positive-number blocks:

- Move `right` to include a new block and multiply it into the product.
- If the product becomes too large, move `left` and divide out blocks.
- Once the product is below `k`, count every valid subarray ending at `right`.

Because all values are positive, adding factors never makes the product smaller, and removing factors never makes it larger.

## Why return zero when `k <= 1`?

Every element is positive, so every non-empty subarray product is at least `1`.

The required condition is strict:

```text
product < k
```

If `k` is `1` or smaller, no non-empty product can qualify:

```python
if k <= 1:
    return 0
```

## Expand the right edge

```python
current_product *= nums[right]
```

This includes the newest value in the window.

## Shrink invalid windows

```python
while current_product >= k:
    current_product //= nums[left]
    left += 1
```

Use `while`, not `if`, because removing one value might not be enough to make the product smaller than `k`.

## Why use `//` instead of `/`?

In Python 3:

```text
20 / 5  = 4.0  → float
20 // 5 = 4    → integer
```

The current product was built by multiplying every element inside the window. Therefore, `nums[left]` is guaranteed to be one of its exact factors.

For example:

```text
window = [10, 5, 2]
current_product = 10 × 5 × 2 = 100
```

Remove the leftmost `10`:

```text
100 // 10 = 10
```

The remaining window is `[5, 2]`, whose exact product is `10`.

No uneven rounding occurs. Integer division simply reverses one earlier multiplication.

Using `/` would unnecessarily change the product into a float:

```text
100 → 10.0 → 2.0
```

Floats can introduce precision concerns for large values. `//` keeps every product exact and integral:

```text
100 → 10 → 2
```

> **Division memory rule: we are removing an exact factor from an integer product, so use `//`.**

## Why add `right - left + 1`?

After shrinking, the entire window from `left` through `right` has a product below `k`.

Because all numbers are positive, removing values from the left can only keep or reduce the product. Therefore, every suffix of this valid window ending at `right` is also valid.

For:

```text
window = [5, 2, 6]
          L     R
```

All subarrays ending at `right` are:

```text
[6]
[2, 6]
[5, 2, 6]
```

There is one possible start at every index from `left` through `right`:

```python
right - left + 1
```

These subarrays are new because they all end at the current `right` index; previous iterations counted only subarrays ending earlier.

## Implementation with comments

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        # Since every element is positive, every non-empty product is at least
        # 1. No product can be strictly below k when k <= 1.
        if k <= 1:
            return 0

        total_count = 0
        current_product = 1
        left = 0

        # Expand the sliding window using the right pointer.
        for right in range(len(nums)):
            current_product *= nums[right]

            # Shrink from the left until the product is valid again.
            while current_product >= k:
                # nums[left] is an exact factor of current_product, so integer
                # division removes it without rounding or floating-point values.
                current_product //= nums[left]
                left += 1

            # Every subarray ending at right and starting from left through
            # right has a product below k.
            total_count += right - left + 1

        return total_count
```

## Complete dry run

```python
nums = [10, 5, 2, 6]
k = 100
```

Initialize:

```text
left = 0
current_product = 1
total_count = 0
```

### `right = 0`, value `10`

```text
current_product = 1 × 10 = 10
10 < 100 → valid
```

New subarrays ending at index `0`:

```text
[10]
```

```text
new count = 0 - 0 + 1 = 1
total_count = 1
```

### `right = 1`, value `5`

```text
current_product = 10 × 5 = 50
50 < 100 → valid
```

New subarrays ending at index `1`:

```text
[5]
[10, 5]
```

```text
new count = 1 - 0 + 1 = 2
total_count = 1 + 2 = 3
```

### `right = 2`, value `2`

```text
current_product = 50 × 2 = 100
100 >= 100 → invalid
```

Shrink by removing `nums[left] = 10`:

```text
current_product = 100 // 10 = 10
left = 1
```

The valid window is now `[5, 2]`.

New subarrays ending at index `2`:

```text
[2]
[5, 2]
```

```text
new count = 2 - 1 + 1 = 2
total_count = 3 + 2 = 5
```

### `right = 3`, value `6`

```text
current_product = 10 × 6 = 60
60 < 100 → valid
```

The current window is `[5, 2, 6]`.

New subarrays ending at index `3`:

```text
[6]
[2, 6]
[5, 2, 6]
```

```text
new count = 3 - 1 + 1 = 3
total_count = 5 + 3 = 8
```

Return:

```text
8
```

## Why the nested loops are `O(n)`

Although `while` is inside `for`, both pointers only move forward:

- `right` visits each element once.
- `left` removes each element at most once.

Each value is multiplied once and divided out at most once, so the total work is linear.

## Complexity

- Time: `O(n)`
- Extra space: `O(1)`

## Edge cases

- `k <= 1` returns `0`.
- One element may form a valid subarray.
- A large element may force the window to shrink past itself before continuing.
- Every subarray may be valid when `k` is sufficiently large.

## Common mistakes

- Using `/` and unnecessarily converting the exact product into a float.
- Using `if` instead of `while` when shrinking.
- Counting only the entire window instead of all suffixes ending at `right`.
- Forgetting that the inequality is strict: product must be `< k`, not `<= k`.
- Applying this exact sliding window when zero or negative values are allowed under different constraints.

## What I learned

Maintain the longest valid positive-product window ending at each right index, then count all of its suffixes with `right - left + 1`.
