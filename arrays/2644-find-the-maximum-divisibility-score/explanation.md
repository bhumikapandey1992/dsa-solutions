# 2644. Find the Maximum Divisibility Score

## Problem in simple words

For every value in `divisors`, count how many numbers in `nums` it divides perfectly.

The divisor with the largest count wins. If several divisors have the same count, return the smallest divisor among them.

## Math-quiz analogy

Imagine `divisors` is a group of teachers, and every teacher has a favorite divisor. The `nums` array is a test paper containing several numbers.

Each teacher checks the entire paper and asks:

> How many numbers can be divided perfectly by my favorite divisor?

Every perfect division earns that teacher one point:

```python
num % divisor == 0
```

The teacher with the most points becomes the champion. If teachers tie, the teacher with the smaller favorite divisor wins.

## What must be tracked?

```python
max_score = -1
best_divisor = float("inf")
```

- `max_score` is the champion's score so far.
- `best_divisor` is the champion's divisor.

## Why initialize `max_score` to `-1`?

A divisibility score can never be negative. Its smallest possible value is `0`.

Starting at `-1` guarantees that the first divisor becomes the initial champion, even if it divides none of the numbers:

```text
first score = 0
0 > -1 → new champion
```

## Why initialize `best_divisor` to infinity?

Infinity acts like a placeholder larger than every real divisor:

```python
best_divisor = float("inf")
```

Therefore, any real divisor is smaller if an initial tie comparison occurs. Once the first champion is selected, `best_divisor` becomes a normal integer.

## Grade every teacher

```python
for divisor in divisors:
    current_score = 0
```

Each divisor receives a fresh score of zero. Its score must not carry over from the previous divisor.

Then examine every number:

```python
for num in nums:
    if num % divisor == 0:
        current_score += 1
```

The modulo operator returns the remainder after division. A remainder of zero means the number is perfectly divisible:

```text
15 % 5 = 0 → point
9 % 5 = 4  → no point
```

## Scenario A: strictly higher score

```python
if current_score > max_score:
    max_score = current_score
    best_divisor = divisor
```

When the new teacher has more points, both champion variables must be updated.

## Scenario B: tied score

```python
elif current_score == max_score:
    if divisor < best_divisor:
        best_divisor = divisor
```

When the scores are equal, compare only the divisors. The smaller divisor wins the tie.

`max_score` does not need to change because the winning score remains the same.

## Complete dry run

```python
nums = [2, 9, 15, 50]
divisors = [5, 3, 7, 2]
```

### Initialization

```python
max_score = -1
best_divisor = float("inf")
```

```text
Champion: none
Champion score: -1
```

### Teacher 5

```python
divisor = 5
current_score = 0
```

Check every number:

```text
2 % 5  = 2 → no point
9 % 5  = 4 → no point
15 % 5 = 0 → current_score = 1
50 % 5 = 0 → current_score = 2
```

Compare with the champion:

```text
2 > -1 → strictly higher score
```

Update:

```text
max_score = 2
best_divisor = 5
```

### Teacher 3

Reset the temporary score:

```python
current_score = 0
```

```text
2 % 3  = 2 → no point
9 % 3  = 0 → current_score = 1
15 % 3 = 0 → current_score = 2
50 % 3 = 2 → no point
```

Compare:

```text
current_score == max_score → 2 == 2
3 < 5 → teacher 3 wins the tie
```

Update only the divisor:

```text
max_score = 2
best_divisor = 3
```

### Teacher 7

```text
2 % 7  ≠ 0
9 % 7  ≠ 0
15 % 7 ≠ 0
50 % 7 ≠ 0

current_score = 0
```

Compare:

```text
0 < 2 → teacher 7 loses
```

Nothing changes:

```text
max_score = 2
best_divisor = 3
```

### Teacher 2

```text
2 % 2  = 0 → current_score = 1
9 % 2  = 1 → no point
15 % 2 = 1 → no point
50 % 2 = 0 → current_score = 2
```

Compare:

```text
current_score == max_score → 2 == 2
2 < 3 → teacher 2 wins the tie
```

Update:

```text
max_score = 2
best_divisor = 2
```

### Return the champion

```python
return best_divisor
```

```text
return 2
```

## Implementation with comments

```python
class Solution(object):
    def maxDivScore(self, nums, divisors):
        # Start below every possible score so the first divisor becomes the
        # initial champion, even when its score is zero.
        max_score = -1

        # Start with infinity so any real divisor wins an initial score tie.
        best_divisor = float("inf")

        for divisor in divisors:
            current_score = 0

            # Count how many values are perfectly divisible by this divisor.
            for num in nums:
                if num % divisor == 0:
                    current_score += 1

            # A strictly higher score creates a new champion.
            if current_score > max_score:
                max_score = current_score
                best_divisor = divisor

            # If the scores tie, the smaller divisor becomes the champion.
            elif current_score == max_score:
                if divisor < best_divisor:
                    best_divisor = divisor

        return best_divisor
```

The required LeetCode method name is `maxDivScore`.

## Complexity

Let `D` be the number of divisors and `N` the number of values in `nums`.

- Time: `O(D × N)`
- Extra space: `O(1)`

The nested loops check every number once for every divisor.

## Edge cases

- Every divisor has score zero: return the smallest divisor.
- Several divisors share the maximum score: return the smallest one.
- One divisor divides every number.
- The divisors are not sorted; the explicit tie condition still finds the smallest winner.

## Common mistakes

- Forgetting to reset `current_score` for each divisor.
- Updating only `best_divisor` but not `max_score` after a higher score.
- Ignoring the smallest-divisor tie-breaker.
- Assuming the divisors arrive in sorted order.
- Using the wrong method name instead of `maxDivScore`.

## What I learned

Treat each divisor as a contestant: calculate its score independently, replace the champion for a higher score, and use the smaller divisor to break a tie.
