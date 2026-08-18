# 767. Reorganize String

## Problem in simple words

Rearrange the characters of a string so that no two neighboring characters are equal. Return any valid rearrangement. If no valid arrangement exists, return an empty string.

```text
"aab"  → "aba"
"aaab" → ""
```

## The central difficulty

The character with the largest frequency is the hardest one to separate. If we postpone it, too many copies may remain near the end and be forced next to one another.

Therefore, we repeatedly use the most frequent character that is currently safe—but we temporarily prevent the character placed last from being selected again immediately.

This is a greedy strategy supported by a max-heap.

## Full analogy: seating rival fans

Imagine characters are groups of sports fans waiting to enter a row of seats. Fans from the same group may not sit next to each other.

For:

```text
s = "aaabbc"
```

the waiting groups are:

```text
A group: a a a   (3 people)
B group: b b     (2 people)
C group: c       (1 person)
```

The largest group is the most dangerous because it is hardest to separate. The usher follows two rules:

1. Seat someone from the largest available group.
2. Keep that group outside the waiting line for one turn.

The temporary hold guarantees that the next seat receives a different character.

### Seating process

```text
Waiting counts       Held back       Seats
------------------------------------------------
a:3, b:2, c:1        none            _ _ _ _ _ _
```

Choose `a`, the most frequent group:

```text
Waiting: b:2, c:1    Hold: a:2       a _ _ _ _ _
```

Because `a` is held back, choose `b`:

```text
Waiting: c:1, a:2    Hold: b:1       a b _ _ _ _
```

The old held character `a` returned to the heap only after `b` was seated. Now choose `a` again:

```text
Waiting: c:1, b:1    Hold: a:1       a b a _ _ _
```

Continue:

```text
Choose b:            Hold: b:0       a b a b _ _
Choose a:            Hold: a:0       a b a b a _
Choose c:            Hold: c:0       a b a b a c
```

Final result:

```text
"ababac"
```

Every adjacent pair is different.

## Visualizing the one-turn hold

The crucial heap order is:

```text
1. Remove the best available character from the heap.
2. Place it in the result.
3. Return the character from the previous turn to the heap.
4. Hold the character just placed until the next turn.
```

```text
              pop current
                   ↓
MAX HEAP ───────────────→ RESULT
    ↑                       │
    │                       ↓
    └──── return old ─── HOLD CURRENT
          held char          one turn
```

Because the current character remains outside the heap during the next selection, it cannot be placed twice in a row.

## When is an arrangement impossible?

The most frequent character needs enough other characters to separate its copies.

For `"aaab"`:

```text
a _ a _ a
```

There are three `a`s but only one other character available as a separator. We would need two separators, so the arrangement is impossible.

For a string of length `n`, the largest allowed frequency is:

```text
ceil(n / 2) = (n + 1) // 2
```

Therefore:

```python
if maximum_frequency > (len(s) + 1) // 2:
    return ""
```

### Odd-length example

```text
n = 5
largest allowed count = 3

a _ a _ a     valid
```

### Even-length example

```text
n = 4
largest allowed count = 2

a _ a _       valid
```

## Why negative counts are used

Python’s `heapq` removes the smallest item first. We want the character with the largest remaining frequency.

Store counts as negatives:

```text
Real counts:       a:3  b:2  c:1
Heap counts:       a:-3 b:-2 c:-1
```

The smallest negative number is `-3`, so Python pops `a`, which has the largest real count.

After using one `a`:

```python
count += 1
```

Its heap count changes from `-3` to `-2`, meaning two copies remain.

## Step-by-step dry run for `"aab"`

### Count characters

```text
a: 2
b: 1
```

### Create the max-heap

```text
[(-2, "a"), (-1, "b")]
```

### Iteration 1

Pop `a`:

```text
result = "a"
remaining a count = -1
hold = (-1, "a")
heap = [(-1, "b")]
```

### Iteration 2

Only `b` is available because `a` is held back:

```text
result = "ab"
remaining b count = 0
return held a to heap
hold = (0, "b")
heap = [(-1, "a")]
```

### Iteration 3

Pop `a`:

```text
result = "aba"
remaining a count = 0
heap = []
```

Return `"aba"`.

## Implementation

```python
from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        # 1. Count how many times each character appears
        frequencies = Counter(s)

        # 2. If one character occupies too many positions, separation is impossible
        if max(frequencies.values()) > (len(s) + 1) // 2:
            return ""

        # 3. Python has a min-heap, so use negative counts to simulate a max-heap
        max_heap = [(-count, character) for character, count in frequencies.items()]
        heapq.heapify(max_heap)

        result = []

        # 4. Hold back the previously used character for one turn
        previous_count = 0
        previous_character = ""

        while max_heap:
            # 5. Choose the most frequent character that is currently available
            count, character = heapq.heappop(max_heap)
            result.append(character)
            count += 1

            # 6. The previous character is now safe to use again
            if previous_count < 0:
                heapq.heappush(max_heap, (previous_count, previous_character))

            # 7. Hold the current character out of the heap until the next turn
            previous_count = count
            previous_character = character

        return "".join(result)
```

## Line-by-line mental model

```python
frequencies = Counter(s)
```

Count the size of every fan group.

```python
max_heap = [(-count, character) for character, count in frequencies.items()]
heapq.heapify(max_heap)
```

Create a waiting line that always offers the largest group first.

```python
count, character = heapq.heappop(max_heap)
```

Choose the most frequent group that is not currently held back.

```python
result.append(character)
count += 1
```

Seat one character and reduce its remaining frequency.

```python
if previous_count < 0:
    heapq.heappush(max_heap, (previous_count, previous_character))
```

The character used in the previous iteration is now separated by the current character, so it is safe to return it to the heap.

```python
previous_count = count
previous_character = character
```

Hold the character just used outside the heap for the next selection.

## Why the greedy choice works

The most frequent available character creates the greatest future placement risk, so using it early gives us the most remaining positions in which to separate its copies.

The held-back character cannot be selected immediately, guaranteeing different neighbors. Among every other safe character, choosing the most frequent one best balances the remaining counts.

The initial frequency check guarantees that enough separator positions exist. Therefore, the heap process can consume every character without leaving an impossible remainder.

## Complexity

Let `n` be the string length and `k` the number of distinct characters:

- Time: `O(n log k)` because each character is pushed and popped at most once per placement.
- Extra space: `O(k)` for the frequency map and heap, excluding the returned string.

Because the problem uses only lowercase English letters, `k ≤ 26`, so the heap remains small.

## Common mistakes

- Popping the most frequent character twice without holding it back.
- Reinserting the current character before choosing the next character.
- Forgetting to decrease its remaining frequency.
- Using positive counts with Python’s min-heap and accidentally prioritizing the least frequent character.
- Returning a partial result instead of an empty string when separation is impossible.
- Using `len(s) // 2` instead of `(len(s) + 1) // 2` for odd-length strings.

## What I learned

When the most recently used choice is temporarily forbidden, hold it outside the priority queue for one turn. The heap can then select the most urgent remaining safe choice.
