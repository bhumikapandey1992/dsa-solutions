# 1248. Count Number of Nice Subarrays

## Problem in simple words

Count contiguous subarrays containing exactly `k` odd numbers.

Only parity matters:

```text
odd  -> 1
even -> 0
```

The problem becomes counting subarrays whose transformed sum equals `k`.

## Analogy: red and clear beads

Imagine odd numbers as red beads and even numbers as clear beads. While walking across the row, `odd_count` records how many red beads have appeared.

If the current prefix has 5 red beads and an earlier prefix had 2, the section between them contains `5 - 2 = 3` red beads.

For exactly `k` red beads, the earlier prefix we need is:

```text
needed = odd_count - k
```

## Prefix equation

```text
odds in subarray = current prefix odds - earlier prefix odds
```

Set the result equal to `k`:

```text
current - earlier = k
earlier = current - k
```

This directly explains `needed = odd_count - k`.

## Why store frequencies?

Even numbers do not change `odd_count`, so several prefix positions can have the same count. Each occurrence represents a different possible starting boundary.

If the needed count appeared three times, three nice subarrays end at the current index.

## Important lines

### Base case

```python
odd_frequency = {0: 1}
```

This represents the empty prefix before index `0`, where zero odd numbers have been seen. It allows a valid subarray to begin at index `0`.

### Convert parity into a counter

```python
odd_count += num % 2
```

An odd positive integer adds `1`; an even integer adds `0`.

### Find and count matching prefixes

```python
needed = odd_count - k
total_subarrays += odd_frequency.get(needed, 0)
```

Each earlier prefix with `needed` odd values leaves exactly `k` odds between it and the current position.

### Record the current prefix

```python
odd_frequency[odd_count] = odd_frequency.get(odd_count, 0) + 1
```

The current prefix becomes a possible boundary for future subarrays.

## Commented solution

```python
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        odd_frequency = {0: 1}
        odd_count = 0
        total_subarrays = 0

        for num in nums:
            odd_count += num % 2
            needed = odd_count - k
            total_subarrays += odd_frequency.get(needed, 0)
            odd_frequency[odd_count] = odd_frequency.get(odd_count, 0) + 1

        return total_subarrays
```

## Complete dry run

```python
nums = [1, 1, 2, 1, 1]
k = 3
```

Start:

```text
odd_frequency = {0: 1}
odd_count = 0
total = 0
```

| Index | Value | Added | Odd count | Needed | Matches | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | -2 | 0 | 0 |
| 1 | 1 | 1 | 2 | -1 | 0 | 0 |
| 2 | 2 | 0 | 2 | -1 | 0 | 0 |
| 3 | 1 | 1 | 3 | 0 | 1 | 1 |
| 4 | 1 | 1 | 4 | 1 | 1 | 2 |

### Index 0: value `1`

```text
odd_count = 1
needed = 1 - 3 = -2
```

No match exists. Record odd count `1`.

### Index 1: value `1`

```text
odd_count = 2
needed = -1
```

No match exists. Record odd count `2`.

### Index 2: value `2`

The value is even, so `odd_count` remains `2`. No valid subarray ends here, but the frequency of count `2` becomes two because this is a new prefix position.

### Index 3: value `1`

```text
odd_count = 3
needed = 0
```

Count `0` appeared once as the empty prefix. This finds:

```text
[1, 1, 2, 1]
```

The total becomes `1`.

### Index 4: value `1`

```text
odd_count = 4
needed = 1
```

Count `1` appeared once after index `0`. This finds:

```text
[1, 2, 1, 1]
```

The final total is `2`.

## Why the even number matters

Although an even number does not increase the odd count, it creates a new prefix position. Repeated prefix counts provide different starting points, which is why we store frequencies.

## Pattern connection

This is the same prefix-frequency pattern as Subarray Sum Equals K:

- Transform odd to `1` and even to `0`.
- Track the transformed prefix sum.
- Search for `current - k`.

## Complexity

- Time: `O(n)`.
- Space: `O(n)` in the worst case.

## Memory rule

> Treat odd numbers as red beads. At every position, subtract `k` from the current red-bead count and count how many earlier prefixes had that result.
