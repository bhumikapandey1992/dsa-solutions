# 1588. Sum of All Odd Length Subarrays

## Problem in simple words

Return the combined sum of every contiguous subarray whose length is odd.

Instead of building every subarray, calculate how many valid odd-length subarrays contain each element. Then add that element's complete contribution to the answer.

## Subway-photo analogy

Imagine the array is a subway train:

```text
arr   = [5, 4, 3, 2]
index    0  1  2  3
```

A photographer takes pictures of connected sections of the train. Each picture is a subarray. We only keep pictures containing an odd number of cars: one car, three cars, five cars, and so on.

For each train car, ask:

1. How many places can a picture containing this car start?
2. How many places can it end?
3. How many start-and-end combinations are there?
4. How many of those pictures have odd length?
5. How much does this car contribute across those pictures?

## Why `i + 1` counts starting choices

Suppose we are examining value `4` at index `1`:

```text
[5, 4, 3, 2]
    ↑
  index 1
```

A picture containing `4` can start at:

```text
index 0 → [5, 4, ...]
index 1 → [4, ...]
```

There are two choices:

```text
i + 1 = 1 + 1 = 2
```

The index `i` tells us how many elements are strictly before the current element. Adding one includes the current element itself.

We are not checking only the immediate left neighbor. We count every possible starting position from the beginning of the array through index `i`.

> Left memory rule: `i + 1` counts all possible starts from the left edge through me.

## Why `n - i` counts ending choices

The same picture can end at:

```text
index 1 → [..., 4]
index 2 → [..., 4, 3]
index 3 → [..., 4, 3, 2]
```

There are three choices:

```text
n - i = 4 - 1 = 3
```

Subtracting `i` removes the elements strictly before the current position, leaving the current element and everything to its right.

We count every possible ending position through the right edge, not just the immediate right neighbor.

> Right memory rule: `n - i` counts all possible ends from me through the right edge.

## Why multiply the choices?

Every starting choice can pair with every ending choice. For value `4`, the two starts and three ends create six photos:

```text
Start 0, end 1 → [5, 4]
Start 0, end 2 → [5, 4, 3]
Start 0, end 3 → [5, 4, 3, 2]

Start 1, end 1 → [4]
Start 1, end 2 → [4, 3]
Start 1, end 3 → [4, 3, 2]
```

Therefore:

```python
total_subarrays = (i + 1) * (n - i)
```

```text
2 starts × 3 ends = 6 subarrays containing 4
```

> Multiplication memory rule: choose one left edge and one right edge to frame a picture.

## Why `(total_subarrays + 1) // 2`?

The subarray lengths alternate between odd and even as a picture expands:

```text
1 car → odd
2 cars → even
3 cars → odd
4 cars → even
```

For the six subarrays containing `4`, three are odd and three are even:

```text
[5, 4]       length 2 → even
[5, 4, 3]    length 3 → odd
[5, 4, 3, 2] length 4 → even
[4]          length 1 → odd
[4, 3]       length 2 → even
[4, 3, 2]    length 3 → odd
```

When the total is even, the two groups split equally:

```text
(6 + 1) // 2 = 7 // 2 = 3
```

When the total is odd, the odd-length group receives the extra subarray. For five total choices:

```text
Odd, Even, Odd, Even, Odd
```

Without adding one, integer division rounds down incorrectly:

```text
5 // 2 = 2
```

Adding one performs ceiling division by two:

```text
(5 + 1) // 2 = 3
```

For an even total, adding one does not alter the result because integer division discards the remainder:

```text
(6 + 1) // 2 = 3
```

> Odd-count memory rule: divide the photos into odd and even piles; if one is left over, it belongs to the odd pile.

## Why `value * odd_subarrays`?

This is value multiplied by frequency, like counting identical coins.

If value `4` appears in three valid odd-length subarrays, we could add:

```text
4 + 4 + 4 = 12
```

or multiply:

```text
4 × 3 = 12
```

That is what this line does:

```python
total_sum += value * odd_subarrays
```

Expanded:

```python
total_sum = total_sum + (value * odd_subarrays)
```

> Contribution memory rule: value is the coin amount; `odd_subarrays` is how many copies go into the total bucket.

## Implementation with comments

```python
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        total_sum = 0

        for i, value in enumerate(arr):
            # A subarray containing index i can start at any index from 0 to i
            # and end at any index from i to n - 1.
            total_subarrays = (i + 1) * (n - i)

            # Odd and even lengths alternate. Odd lengths receive the extra
            # subarray when the total number of choices is odd.
            odd_subarrays = (total_subarrays + 1) // 2

            # Add this value once for every odd-length subarray containing it.
            total_sum += value * odd_subarrays

        return total_sum
```

## Line-by-line dry run

Use:

```python
arr = [5, 4, 3, 2]
```

### Initialize the array length

```python
n = len(arr)
```

```text
n = 4
```

### Initialize the answer bucket

```python
total_sum = 0
```

```text
total_sum = 0
```

### Iteration 1: `i = 0`, `value = 5`

```python
total_subarrays = (i + 1) * (n - i)
```

```text
=(0 + 1) × (4 - 0)
=1 × 4
=4
```

```python
odd_subarrays = (total_subarrays + 1) // 2
```

```text
=(4 + 1) // 2
=2
```

```python
total_sum += value * odd_subarrays
```

```text
total_sum = 0 + (5 × 2) = 10
```

### Iteration 2: `i = 1`, `value = 4`

```python
total_subarrays = (1 + 1) * (4 - 1)
```

```text
total_subarrays = 2 × 3 = 6
```

```python
odd_subarrays = (6 + 1) // 2
```

```text
odd_subarrays = 3
```

```python
total_sum += 4 * 3
```

```text
total_sum = 10 + 12 = 22
```

### Iteration 3: `i = 2`, `value = 3`

```python
total_subarrays = (2 + 1) * (4 - 2)
```

```text
total_subarrays = 3 × 2 = 6
```

```python
odd_subarrays = (6 + 1) // 2
```

```text
odd_subarrays = 3
```

```python
total_sum += 3 * 3
```

```text
total_sum = 22 + 9 = 31
```

### Iteration 4: `i = 3`, `value = 2`

```python
total_subarrays = (3 + 1) * (4 - 3)
```

```text
total_subarrays = 4 × 1 = 4
```

```python
odd_subarrays = (4 + 1) // 2
```

```text
odd_subarrays = 2
```

```python
total_sum += 2 * 2
```

```text
total_sum = 31 + 4 = 35
```

### Return the result

```python
return total_sum
```

```text
return 35
```

Verify by listing the odd-length subarrays:

```text
Length 1: [5], [4], [3], [2]
Sum = 5 + 4 + 3 + 2 = 14

Length 3: [5, 4, 3], [4, 3, 2]
Sum = 12 + 9 = 21

Grand total = 14 + 21 = 35
```

## Complexity

- Time: `O(n)`
- Extra space: `O(1)`

## Edge cases

- One element contributes once.
- When the element's total number of containing subarrays is odd, the odd-length count receives the extra one.
- Elements near the middle generally appear in more subarrays than elements at the edges.

## Common mistakes

- Treating `i + 1` and `n - i` as only the immediate neighbors rather than every boundary choice.
- Forgetting the `+1` that rounds an odd total upward.
- Adding `value` only once instead of multiplying it by its frequency.
- Generating all subarrays when a contribution count produces an `O(n)` solution.

## What I learned

For each train car, count all possible left edges, count all possible right edges, combine them, keep the odd-sized photos, and multiply the car's value by how often it appears.
