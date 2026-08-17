# 2357. Make Array Zero by Subtracting Equal Amounts

## Problem in simple words

We are given an array of non-negative integers. During one operation:

1. Choose a positive number `x` that is no larger than the smallest non-zero number currently in the array.
2. Subtract `x` from every positive array element.

Return the minimum number of operations required to turn every element into zero.

## Example

```text
nums = [1, 5, 0, 3, 5]
```

One optimal sequence is:

```text
[1, 5, 0, 3, 5]
 subtract 1
        ↓
[0, 4, 0, 2, 4]
 subtract 2
        ↓
[0, 2, 0, 0, 2]
 subtract 2
        ↓
[0, 0, 0, 0, 0]
```

The answer is `3`.

## The key observation

We do not need to simulate every subtraction.

The original array contains these distinct positive values:

```text
{1, 3, 5}
```

There are three different positive levels, so exactly three operations are required.

```text
minimum operations = number of distinct positive values
```

For the example:

```text
len({1, 3, 5}) = 3
```

## Final mental model

The reasoning can be remembered like this:

> In every operation, choose the current smallest positive number as `x`. That value is guaranteed to become zero. Then choose the new smallest positive number and repeat. Equal values become zero together, so every distinct positive value requires exactly one operation.

For the example:

```text
Original:          [1, 5, 0, 3, 5]
Smallest positive:  1
Subtract 1:        [0, 4, 0, 2, 4]   original level 1 is gone

Smallest positive:  2
Subtract 2:        [0, 2, 0, 0, 2]   original level 3 is gone

Smallest positive:  2
Subtract 2:        [0, 0, 0, 0, 0]   original level 5 is gone
```

This gives a direct correspondence:

```text
Distinct positive values:  {1, 3, 5}
                              ↓  ↓  ↓
Operations required:          1  2  3
```

### Why choose the current minimum?

The rules allow choosing an `x` smaller than the current smallest positive number. However, that would make no element reach zero.

For example, if the current positives are `{3, 5}` and we choose `x = 1`:

```text
{3, 5} - 1 = {2, 4}
```

Both values are still positive, so we used an operation without eliminating a level. That cannot be part of a minimum-operation strategy.

Choosing the current minimum is optimal because it guarantees progress:

```text
{3, 5} - 3 = {0, 2}
```

### Why can only one distinct level disappear at a time?

One operation subtracts the same `x` from every positive value. Distinct values keep the same distance from one another:

```text
Before:             5 - 3 = 2
After subtracting 1: 4 - 2 = 2
```

Also, `x` cannot be greater than the smallest positive value. Therefore:

- the current smallest positive value can reach zero;
- every larger distinct value must remain positive;
- duplicate copies of the smallest value all reach zero together.

That is the precise reason the answer is the number of distinct positive values—not the number of elements and not the sum of the values.

## Full analogy: lowering stacks one floor at a time

Imagine every number as the height of a building made from blocks:

```text
nums = [1, 5, 0, 3, 5]

          █           █
          █           █       height 5
          █           █
          █     █     █       height 3
    █     █     █     █       height 1
   ─────────────────────
    1     5     0  3  5
```

In one operation, we lower every building that is still standing by the same amount. The shortest positive building reaches the ground first.

### Operation 1: remove the first height level

The smallest positive value is `1`, so subtract `1` from every positive element:

```text
Before:       [1, 5, 0, 3, 5]
Subtract:      1  1  0  1  1
               ↓  ↓     ↓  ↓
After:        [0, 4, 0, 2, 4]
```

All buildings that originally had height `1` have now disappeared.

### Operation 2: remove the next height level

The smallest remaining positive value is `2`. Subtract `2`:

```text
Before:       [0, 4, 0, 2, 4]
Subtract:      0  2  0  2  2
                  ↓     ↓  ↓
After:        [0, 2, 0, 0, 2]
```

These zeroed elements were originally at height `3`:

```text
original height 3 - previous 1 - current 2 = 0
```

### Operation 3: remove the final height level

The smallest remaining positive value is `2` again:

```text
Before:       [0, 2, 0, 0, 2]
Subtract:      0  2  0  0  2
                  ↓        ↓
After:        [0, 0, 0, 0, 0]
```

These were the buildings whose original height was `5`.

### What the layers reveal

Although the subtraction amounts were `1`, `2`, and `2`, each operation eliminated one original positive height:

```text
Original distinct heights:     1       3       5
                                ↓       ↓       ↓
Eliminated by operation:        1       2       3
```

Duplicate heights disappear together. Both `5`s always remain equal because every operation subtracts the same amount from both of them.

```text
two equal values
      5          5
      ↓ -1       ↓ -1
      4          4
      ↓ -2       ↓ -2
      2          2
      ↓ -2       ↓ -2
      0          0
```

Therefore, duplicates do not add extra operations. Only the number of different positive heights matters.

## Why the formula is correct

Let the sorted distinct positive values be:

```text
v1 < v2 < v3 < ... < vk
```

The optimal operations remove the gaps between these levels:

```text
Operation 1 subtracts:  v1
Operation 2 subtracts:  v2 - v1
Operation 3 subtracts:  v3 - v2
...
Operation k subtracts:  vk - v(k-1)
```

Each subtraction is positive and is equal to the smallest non-zero value at that moment, so every operation is valid.

After each operation, at least one distinct positive level becomes zero. There are `k` such levels, so `k` operations are sufficient.

They are also necessary: one valid operation can eliminate only the current smallest positive level. Larger distinct values remain positive because the chosen `x` cannot exceed that smallest level. Therefore, fewer than `k` operations cannot eliminate all `k` distinct positive levels.

Hence:

```text
minimum operations = k = count of distinct positive values
```

## Why zero is ignored

The operation subtracts only from positive elements. A zero is already finished and never changes.

For example:

```text
nums = [0]
positive values = {}
answer = 0
```

This is why we add a number to the set only when `number > 0`.

## Why a set is useful

A set stores each value only once:

```text
Array:              [1, 5, 0, 3, 5]
Positive values:     1  5     3  5
Remove duplicates:  {1, 3, 5}
Count:                3
```

The repeated `5` is automatically represented once.

## Implementation

```python
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        # A set automatically removes duplicates
        # Subtracting {0} ensures we only count strictly positive numbers
        return len(set(nums) - {0})
```

## Line-by-line explanation

The entire solution is one expression:

```python
len(set(nums) - {0})
```

Read it from the inside outward.

### 1. `set(nums)` removes duplicates

```python
set(nums)
```

For the example:

```text
nums = [1, 5, 0, 3, 5]
              ↓ set(nums)
       {0, 1, 3, 5}
```

The repeated `5` appears only once. This matches the problem because equal values always become zero during the same operation.

### 2. `{0}` is a set containing zero

```python
{0}
```

The braces here do not mean an empty dictionary. They create a set with one member: zero.

### 3. Set subtraction removes zero

```python
set(nums) - {0}
```

The `-` operator means set difference: keep everything in the left set except values found in the right set.

```text
{0, 1, 3, 5} - {0} = {1, 3, 5}
```

Because the problem guarantees non-negative integers, removing zero leaves exactly the distinct positive values.

### 4. `len(...)` counts the required operations

```python
len({1, 3, 5}) = 3
```

Each distinct positive value represents one level that must be eliminated, so the set’s size is the minimum number of operations.

### Complete evaluation

```text
nums                         = [1, 5, 0, 3, 5]
set(nums)                    = {0, 1, 3, 5}
set(nums) - {0}              = {1, 3, 5}
len(set(nums) - {0})         = 3
```

## Why this version is better than simulation

The code does not need to:

- repeatedly find the smallest positive number;
- modify every positive element;
- track each intermediate array;
- sort the numbers.

It goes directly to the invariant that determines the answer: the number of distinct positive levels.

This compact version and the explicit loop version have the same average complexity. The one-line version is preferable here because the set expression closely matches the mathematical insight.

## Complexity

For an array containing `n` values:

- Time: `O(n)` on average because we scan the array once and set insertion is `O(1)` on average.
- Extra space: `O(k)`, where `k` is the number of distinct positive values.

Under this problem’s small numeric constraints, a fixed-size boolean structure could also work, but the set solution expresses the observation most clearly.

## Common mistakes

- Counting every positive element instead of every distinct positive value.
- Forgetting `- {0}` and returning one operation for an already-zero array.
- Simulating repeated subtraction even though only the distinct original levels matter.
- Sorting the whole array when a set alone is enough.
- Assuming duplicate values require separate operations; equal values always reach zero together.
- Confusing `{0}` with `{}`: `{0}` is a one-element set, while `{}` is an empty dictionary.

## What I learned

When one operation changes every positive value equally, differences between values are preserved until smaller levels disappear. Look for distinct levels instead of simulating every state change.
