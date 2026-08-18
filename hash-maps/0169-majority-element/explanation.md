# 169. Majority Element

## Problem in simple words

Given an array, return the value that appears more than half the time.

The problem guarantees that a majority element always exists.

```text
nums = [2, 2, 1, 1, 1, 2, 2]

2 appears 4 times
array length = 7
half = 7 // 2 = 3

4 > 3, so the majority element is 2.
```

## What “majority” means

The majority element appears strictly more than `n / 2` times.

In integer arithmetic, the condition is:

```python
frequency > len(nums) // 2
```

The word **strictly** matters. Appearing exactly half the time is not enough.

```text
n = 6
n // 2 = 3

count 3 → not a majority
count 4 → majority
```

## The strategy

Use a dictionary to count how many times every number has appeared so far.

After increasing a number’s count, immediately check whether it has crossed the majority threshold. As soon as it does, return it.

```text
read number → update its count → compare with half → return if majority
```

## Full analogy: election night

Imagine each array value is a candidate and each occurrence is one ballot.

For:

```text
[2, 2, 1, 1, 1, 2, 2]
```

there are seven ballots. A candidate needs more than half:

```text
half of 7 using integer division = 3
votes required to win a majority = 4
```

The dictionary is the live election scoreboard.

### Count ballots as they arrive

```text
Ballot     Updated scoreboard       Majority yet?
---------------------------------------------------
   2       {2: 1}                   No
   2       {2: 2}                   No
   1       {2: 2, 1: 1}             No
   1       {2: 2, 1: 2}             No
   1       {2: 2, 1: 3}             No
   2       {2: 3, 1: 3}             No
   2       {2: 4, 1: 3}             Yes: 4 > 3
```

As soon as candidate `2` reaches four votes, the election is decided and we return `2`.

## Why early return is safe

Once a number’s count is greater than half of the total array length, it is already the majority element. Future values cannot undo occurrences that have already been counted.

Also, two different numbers cannot both appear more than half the time:

```text
more than half + more than half > the entire array
```

Therefore, the first value that crosses the threshold must be the unique answer.

## Understanding `count.get(num, 0)`

```python
count[num] = count.get(num, 0) + 1
```

This handles both new and previously seen values.

For a new number:

```text
count.get(num, 0) returns 0
0 + 1 = 1
```

For an existing number with count `3`:

```text
count.get(num, 0) returns 3
3 + 1 = 4
```

It is a compact version of:

```python
if num not in count:
    count[num] = 0

count[num] += 1
```

## Complete dry run: `[3, 2, 3]`

```text
n = 3
threshold = 3 // 2 = 1
```

### Read the first `3`

```text
count = {3: 1}
1 > 1? No
```

### Read `2`

```text
count = {3: 1, 2: 1}
1 > 1? No
```

### Read the second `3`

```text
count = {3: 2, 2: 1}
2 > 1? Yes
```

Return `3`.

## Why `>` is used instead of `>=`

Consider:

```text
nums = [1, 1, 2, 2]
n = 4
n // 2 = 2
```

Neither value is a majority because neither appears more than twice.

If we used:

```python
count[num] >= len(nums) // 2
```

we would incorrectly declare a number with exactly half the positions as the majority.

The correct condition is:

```python
count[num] > len(nums) // 2
```

## Implementation

```python
class Solution(object):
    def majorityElement(self, nums):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

            if count[num] > len(nums) // 2:
                return num
```

## Line-by-line mental model

```python
count = {}
```

Create an empty election scoreboard.

```python
for num in nums:
```

Process every ballot.

```python
count[num] = count.get(num, 0) + 1
```

Add one vote to the current candidate.

```python
if count[num] > len(nums) // 2:
    return num
```

Return as soon as the candidate has strictly more than half of all possible votes.

## Edge cases

### One element

```text
nums = [7]
threshold = 1 // 2 = 0
count of 7 = 1
1 > 0 → return 7
```

### Negative majority

Dictionary keys may be negative:

```text
nums = [-1, -1, -1, 2, 3]
answer = -1
```

### Even array length

For length `6`, a majority needs at least `4` occurrences—not `3`.

## Complexity

Let `n` be the array length:

- Time: `O(n)` in the worst case because each element is processed once.
- Extra space: `O(m)`, where `m` is the number of distinct values; worst-case `O(n)`.

The Boyer-Moore Voting Algorithm can solve the problem using `O(1)` extra space, but this frequency-map version is direct and easy to verify.

## Common mistakes

- Using `>=` instead of `>` for the majority condition.
- Comparing against the number of distinct values instead of the total array length.
- Forgetting to initialize a new dictionary key before incrementing it.
- Returning the most frequent value without checking that it exceeds half.
- Assuming the input must be sorted.
- Forgetting that the problem guarantees a majority element exists.

## What I learned

When a problem defines a winner by a strict frequency threshold, update the count and test the threshold immediately. A proof that only one value can cross it makes early return safe.
