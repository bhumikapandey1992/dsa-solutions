# 347. Top K Frequent Elements

## Problem in simple words

Given an integer array and a number `k`, return the `k` values that appear most frequently.

For example:

```text
nums = [1, 1, 1, 2, 2, 3]
k = 2
```

The frequencies are:

```text
1 appears 3 times
2 appears 2 times
3 appears 1 time
```

The two most frequent values are `[1, 2]`.

## The two-part strategy

The solution separates the problem into two clear jobs:

1. Count how often every distinct number appears.
2. Sort the `(number, frequency)` pairs from highest frequency to lowest and take the first `k` numbers.

```text
array → frequency map → sorted leaderboard → first k values
```

## Full analogy: a popularity leaderboard

Imagine every number is a contestant receiving votes. Each occurrence in the array is one vote.

For:

```text
[1, 1, 1, 2, 2, 3]
```

the ballot box contains:

```text
Vote 1: contestant 1
Vote 2: contestant 1
Vote 3: contestant 1
Vote 4: contestant 2
Vote 5: contestant 2
Vote 6: contestant 3
```

### Stage 1: count the votes

The dictionary is the scoreboard:

```text
┌────────────┬───────┐
│ Contestant │ Votes │
├────────────┼───────┤
│     1      │   3   │
│     2      │   2   │
│     3      │   1   │
└────────────┴───────┘
```

In Python:

```python
count = {
    1: 3,
    2: 2,
    3: 1,
}
```

### Stage 2: rank the contestants

`count.items()` produces `(number, frequency)` pairs:

```text
[(1, 3), (2, 2), (3, 1)]
```

Sort by the frequency at index `1`, in descending order:

```text
Rank 1: (1, 3)   ███
Rank 2: (2, 2)   ██
Rank 3: (3, 1)   █
```

If `k = 2`, award the top two positions:

```text
Winners: [1, 2]
```

We return the contestant numbers, not their vote counts.

## Building the frequency map

```python
count[num] = count.get(num, 0) + 1
```

`count.get(num, 0)` means:

- return the current count if `num` is already in the dictionary;
- otherwise, start with the default value `0`.

Then add one for the current occurrence.

For the first three `1`s:

```text
First 1:  get(1, 0) = 0 → count[1] = 1
Second 1: get(1, 0) = 1 → count[1] = 2
Third 1:  get(1, 0) = 2 → count[1] = 3
```

## Understanding the sorting expression

```python
sorted_items = sorted(
    count.items(),
    key=lambda x: x[1],
    reverse=True,
)
```

### `count.items()`

Produces pairs shaped like:

```text
(number, frequency)
```

For example:

```text
(1, 3)
```

Here:

- `x[0]` is the number `1`;
- `x[1]` is its frequency `3`.

### `key=lambda x: x[1]`

The sorting key says:

> Rank each pair using its frequency, which is stored at index `1`.

Without this key, Python would primarily sort by the number itself, which is not what the problem asks.

### `reverse=True`

Sort from largest frequency to smallest frequency:

```text
3, 2, 1
```

rather than:

```text
1, 2, 3
```

## Complete dry run

Given:

```text
nums = [1, 1, 1, 2, 2, 3]
k = 2
```

### Count every value

```text
Read 1 → {1: 1}
Read 1 → {1: 2}
Read 1 → {1: 3}
Read 2 → {1: 3, 2: 1}
Read 2 → {1: 3, 2: 2}
Read 3 → {1: 3, 2: 2, 3: 1}
```

### Convert to pairs

```text
count.items() = [(1, 3), (2, 2), (3, 1)]
```

### Sort by frequency

```text
sorted_items = [(1, 3), (2, 2), (3, 1)]
```

### Extract the first `k` numbers

```text
i = 0 → sorted_items[0][0] = 1 → result = [1]
i = 1 → sorted_items[1][0] = 2 → result = [1, 2]
```

Return `[1, 2]`.

## Implementation

```python
class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        sorted_items = sorted(
            count.items(),
            key=lambda x: x[1],
            reverse=True,
        )
        result = []

        for i in range(k):
            result.append(sorted_items[i][0])

        return result
```

## Line-by-line mental model

```python
count = {}
```

Create an empty scoreboard.

```python
for num in nums:
    count[num] = count.get(num, 0) + 1
```

Give one vote to every number encountered.

```python
count.items()
```

Turn the scoreboard into `(number, frequency)` pairs.

```python
key=lambda x: x[1]
```

Tell Python to compare the frequency portion of every pair.

```python
reverse=True
```

Put the highest frequencies first.

```python
for i in range(k):
    result.append(sorted_items[i][0])
```

Visit the first `k` leaderboard entries and collect the number stored at pair index `0`.

## Edge cases

### One value

```text
nums = [1]
k = 1
answer = [1]
```

### Negative numbers

Dictionary keys may be negative:

```text
nums = [-1, -1, 2]
k = 1
answer = [-1]
```

### `k` equals the number of distinct values

Every distinct number is returned.

### Equal frequencies

If multiple values have the same frequency, any valid ordering among them is acceptable as long as the returned values satisfy the top-`k` requirement guaranteed by the problem.

## Complexity

Let:

- `n` be the number of elements in `nums`;
- `m` be the number of distinct values.

Then:

- Counting costs `O(n)`.
- Sorting `m` dictionary entries costs `O(m log m)`.
- Collecting the first `k` values costs `O(k)`.

Overall:

- Time: `O(n + m log m)`; in the worst case, `O(n log n)`.
- Extra space: `O(m)` for the frequency dictionary and sorted pairs.

This is a clear sorting-based solution. A heap or bucket-sort version can improve the asymptotic selection step, but the dictionary-plus-sort approach is straightforward and easy to reason about.

## Common mistakes

- Sorting the original array values rather than the frequency pairs.
- Using `x[0]` as the sorting key, which sorts by number instead of frequency.
- Forgetting `reverse=True` and selecting the least frequent values.
- Appending `sorted_items[i][1]`, which returns the frequency instead of the number.
- Counting with `count[num] += 1` before initializing a missing key.
- Returning every sorted pair instead of only the first `k` numbers.

## What I learned

When a problem asks for the most common items, first separate identity from frequency with a hash map. Then rank the `(item, frequency)` pairs by the frequency field.
