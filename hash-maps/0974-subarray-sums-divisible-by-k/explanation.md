# 974. Subarray Sums Divisible by K

## Problem in simple words

Count the contiguous subarrays whose sum is divisible by `k`.

We use prefix sums, but we store only their remainders instead of their complete values.

## Analogy: walking around a remainder clock

Imagine a circular clock with `k` positions labeled:

```text
0, 1, 2, ..., k - 1
```

As numbers are added to the running sum, `running_sum % k` tells us our position on the clock.

If we arrive at a position visited earlier, the distance traveled between those visits must contain a whole number of complete circles. Therefore, the sum between those prefix positions is divisible by `k`.

> Same remainder means the difference has remainder zero.

## Why matching remainders work

Suppose two prefix sums have remainder `r`:

```text
earlier_sum = a * k + r
current_sum = b * k + r
```

Their difference is the intervening subarray sum:

```text
current_sum - earlier_sum
= (b * k + r) - (a * k + r)
= (b - a) * k
```

The identical remainders cancel. The result is a multiple of `k`.

## Why store frequencies rather than only one index?

This problem asks for the number of subarrays, not the longest one.

If the current remainder appeared three times earlier, each earlier prefix creates a different valid subarray ending here. Therefore, we add all three:

```python
total_subarrays += remainder_counts[remainder]
```

## Critical base case

Array version:

```python
remainder_counts[0] = 1
```

Dictionary version:

```python
remainder_counts = {0: 1}
```

This represents an imaginary empty prefix immediately before index `0`:

```text
prefix sum = 0
remainder = 0
```

If a running sum itself is divisible by `k`, its remainder is `0` and it matches this empty prefix. That correctly counts a subarray beginning at index `0`.

Without the base case, those subarrays would be missed.

## Solution 1: remainder-count array

```python
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        remainder_counts = [0] * k
        remainder_counts[0] = 1

        running_sum = 0
        total_subarrays = 0

        for num in nums:
            running_sum += num
            remainder = running_sum % k

            total_subarrays += remainder_counts[remainder]
            remainder_counts[remainder] += 1

        return total_subarrays
```

### Why an array works

With positive `k`, Python produces remainders from `0` through `k - 1`. Those values can be used directly as array indices.

Advantages:

- direct lookup;
- compact code;
- no hashing overhead.

The array allocates all `k` positions even if some remainders never appear.

## Solution 2: dictionary

```python
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        remainder_counts = {0: 1}

        running_sum = 0
        total_subarrays = 0

        for num in nums:
            running_sum += num
            remainder = running_sum % k

            if remainder in remainder_counts:
                total_subarrays += remainder_counts[remainder]

            remainder_counts[remainder] = remainder_counts.get(remainder, 0) + 1

        return total_subarrays
```

### Why keep the dictionary version?

The dictionary stores only remainders that actually appear. It also resembles other prefix-frequency problems such as Subarray Sum Equals K, making the shared pattern easier to recognize.

Both versions have the same algorithm and produce the same answer.

## Important line-by-line reasoning

### Extend the prefix

```python
running_sum += num
```

This is the sum from index `0` through the current index.

### Find the clock position

```python
remainder = running_sum % k
```

We do not care how many complete groups of `k` are in the prefix. We only need its leftover remainder.

### Count before recording

```python
total_subarrays += remainder_counts[remainder]
```

Only earlier prefixes should pair with the current prefix. Each matching earlier prefix defines one valid starting boundary.

### Record the current prefix

```python
remainder_counts[remainder] += 1
```

After counting, save the current clock position so future prefixes can pair with it.

## Complete dry run

```python
nums = [4, 5, 0, -2, -3, 1]
k = 5
```

Initialize:

```text
remainder_counts = [1, 0, 0, 0, 0]
running_sum = 0
total_subarrays = 0
```

The initial `1` at remainder `0` is the empty prefix.

| Number | Running sum | Remainder | Earlier matches | Added | Total |
|---:|---:|---:|---:|---:|---:|
| 4 | 4 | 4 | 0 | 0 | 0 |
| 5 | 9 | 4 | 1 | 1 | 1 |
| 0 | 9 | 4 | 2 | 2 | 3 |
| -2 | 7 | 2 | 0 | 0 | 3 |
| -3 | 4 | 4 | 3 | 3 | 6 |
| 1 | 5 | 0 | 1 | 1 | 7 |

### Read `4`

```text
running_sum = 4
remainder = 4
```

Remainder `4` has no earlier visits, so add zero. Then record the visit:

```text
remainder_counts = [1, 0, 0, 0, 1]
total = 0
```

### Read `5`

```text
running_sum = 9
remainder = 4
```

Remainder `4` appeared once. The difference between the prefix sums is:

```text
9 - 4 = 5
```

So `[5]` is one valid subarray:

```text
total = 1
remainder_counts[4] = 2
```

### Read `0`

```text
running_sum = 9
remainder = 4
```

There are two earlier remainder-`4` prefixes, producing two new subarrays:

```text
[0]
[5, 0]
```

```text
total = 3
remainder_counts[4] = 3
```

### Read `-2`

```text
running_sum = 7
remainder = 2
```

No earlier remainder `2` exists, so add zero and record it.

### Read `-3`

```text
running_sum = 4
remainder = 4
```

Remainder `4` appeared three times, so three valid subarrays end here:

```text
total = 3 + 3 = 6
```

### Read `1`

```text
running_sum = 5
remainder = 0
```

Remainder `0` already has the imaginary empty-prefix occurrence. This counts the entire array because its sum is divisible by `5`:

```text
total = 6 + 1 = 7
```

Final answer:

```text
7
```

## Negative numbers in Python

Python normalizes modulo by a positive `k` into the range `0` through `k - 1`:

```python
-2 % 5 == 3
```

Therefore, negative numbers are safe for both the array and dictionary versions.

In a language where `%` can return a negative remainder, normalize with:

```text
((running_sum % k) + k) % k
```

## Complexity

- Time: `O(n)` for both solutions.
- Space: `O(k)` because there are only `k` possible normalized remainders.

## Memory rule

> If two prefix sums land at the same position on the remainder clock, the subarray between them traveled complete circles and is divisible by `k`.
