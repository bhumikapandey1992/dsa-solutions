# 128. Longest Consecutive Sequence

## Problem in simple words

Given an unsorted array of integers, find the length of the longest sequence of consecutive values.

The values must be numerically consecutive, but they do not need to appear next to each other in the original array.

```text
Input:  [100, 4, 200, 1, 3, 2]

Consecutive sequence: 1, 2, 3, 4
Answer: 4
```

The problem asks for an `O(n)` solution, so sorting the array is not the intended approach.

## The key observation

Every consecutive sequence has exactly one starting number.

For the sequence:

```text
1 → 2 → 3 → 4
```

`1` is the start because its predecessor, `0`, is missing.

The other values are not starts:

```text
2 has predecessor 1
3 has predecessor 2
4 has predecessor 3
```

Therefore, begin counting only when:

```python
(num - 1) not in num_set
```

This prevents us from recounting the same sequence from every value inside it.

## Full analogy: numbered train cars

Imagine every distinct number is a train car with its number painted on the side.

```text
Input cars:  [100] [4] [200] [1] [3] [2]
```

Place the cars in a large rail yard where we can instantly ask whether a particular numbered car exists. The set is that rail yard.

```text
num_set = {1, 2, 3, 4, 100, 200}
```

Cars form a train when their numbers connect consecutively:

```text
[1]—[2]—[3]—[4]      [100]      [200]
```

We should measure a train only from its engine—the first car with no predecessor.

### Finding the engines

For each car, look for the car immediately before it:

```text
Car 1:   Is car 0 present?   No  → engine
Car 2:   Is car 1 present?   Yes → middle car, skip
Car 3:   Is car 2 present?   Yes → middle car, skip
Car 4:   Is car 3 present?   Yes → last car, skip
Car 100: Is car 99 present?  No  → engine
Car 200: Is car 199 present? No  → engine
```

Only `1`, `100`, and `200` begin trains.

### Measure from engine `1`

```text
Start: [1]                      length 1
Find 2: [1]—[2]                length 2
Find 3: [1]—[2]—[3]            length 3
Find 4: [1]—[2]—[3]—[4]        length 4
Find 5: missing                 stop
```

The train length is `4`.

### Measure the remaining engines

```text
[100]   next car 101 missing   length 1
[200]   next car 201 missing   length 1
```

The longest train contains four cars, so return `4`.

## Why use a set?

The algorithm repeatedly asks questions such as:

```text
Is num - 1 present?
Is current_num + 1 present?
```

A set answers membership questions in average `O(1)` time.

```python
num_set = set(nums)
```

It also removes duplicates automatically. Repeated copies of a number do not make a consecutive sequence longer.

```text
[1, 2, 2, 3]

Distinct sequence: 1, 2, 3
Length: 3, not 4
```

## Complete dry run

Given:

```text
nums = [100, 4, 200, 1, 3, 2]
```

Create the set:

```text
num_set = {1, 2, 3, 4, 100, 200}
longest_streak = 0
```

The exact iteration order of a set is not important. Conceptually:

### Consider `1`

```text
1 - 1 = 0
0 is not in the set → sequence start
```

Walk forward:

```text
current_num = 1, current_streak = 1
2 exists → current_num = 2, current_streak = 2
3 exists → current_num = 3, current_streak = 3
4 exists → current_num = 4, current_streak = 4
5 missing → stop
```

```text
longest_streak = max(0, 4) = 4
```

### Consider `2`, `3`, and `4`

```text
2 has predecessor 1 → skip
3 has predecessor 2 → skip
4 has predecessor 3 → skip
```

The chain is not scanned again.

### Consider `100`

```text
99 missing → start
101 missing → sequence length 1
longest_streak remains 4
```

### Consider `200`

```text
199 missing → start
201 missing → sequence length 1
longest_streak remains 4
```

Return `4`.

## Implementation

```python
class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
```

## Line-by-line mental model

```python
num_set = set(nums)
```

Create an `O(1)`-average lookup structure and remove duplicates.

```python
longest_streak = 0
```

An empty input has no sequence, so zero is the correct initial answer.

```python
for num in num_set:
```

Visit every distinct number.

```python
if (num - 1) not in num_set:
```

Start walking only from the first number of a sequence.

```python
current_num = num
current_streak = 1
```

The starting number itself gives the sequence a length of one.

```python
while (current_num + 1) in num_set:
    current_num += 1
    current_streak += 1
```

Follow consecutive values until the next one is missing.

```python
longest_streak = max(longest_streak, current_streak)
```

Keep the best sequence length seen so far.

## Why the nested loop is still O(n)

At first glance, a `while` loop inside a `for` loop may look like `O(n²)`. The start check prevents that.

For:

```text
1 → 2 → 3 → 4
```

the `while` loop runs only when the outer loop reaches `1`. The outer iterations for `2`, `3`, and `4` fail the start check and do no forward walking.

```text
1: walk through 1, 2, 3, 4
2: skip
3: skip
4: skip
```

Across the complete algorithm, every number participates in at most one forward sequence walk. The total amount of walking is therefore proportional to the number of distinct values.

## Edge cases

### Empty array

```text
nums = []
num_set = {}
answer = 0
```

### One number

```text
nums = [7]
sequence = [7]
answer = 1
```

### Duplicates

```text
nums = [1, 2, 2, 3]
num_set = {1, 2, 3}
answer = 3
```

### Negative values

```text
nums = [-2, -1, 0, 1]
sequence = -2, -1, 0, 1
answer = 4
```

### Several separate sequences

```text
nums = [10, 11, 1, 2, 3, 20]

sequences:
10, 11       length 2
1, 2, 3      length 3
20           length 1

answer = 3
```

## Complexity

Let `n` be the number of input elements:

- Building the set: `O(n)` average time.
- Finding and walking all sequences: `O(n)` average total time.
- Overall time: `O(n)` average.
- Extra space: `O(n)` for the set.

## Common mistakes

- Sorting the input, which produces an `O(n log n)` solution rather than the requested `O(n)` approach.
- Starting a sequence walk from every number and repeatedly scanning the same chain.
- Checking for `num + 1` to identify a start; the start is identified by a missing predecessor, `num - 1`.
- Counting duplicate values as additional consecutive elements.
- Initializing `current_streak` to zero even though the start already counts as one.
- Forgetting that consecutive means numeric order, not adjacency in the original array.

## What I learned

Before traversing a chain, identify a property that only its first element has. Starting exclusively at true boundaries prevents repeated work and can turn an apparent nested-loop solution into linear time.
