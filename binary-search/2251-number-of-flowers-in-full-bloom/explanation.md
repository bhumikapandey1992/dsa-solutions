# 2251. Number of Flowers in Full Bloom

## Problem in simple words

Each flower blooms during an inclusive interval:

```text
[start, end]
```

A person arriving at time `t` sees that flower when:

```text
start <= t <= end
```

Return the number of flowers each person sees.

## Core counting idea

At any time:

```text
flowers currently blooming
= flowers that have started
- flowers that ended earlier
```

The important word is **earlier**. A flower ending exactly when a person arrives is still blooming because the interval includes its ending time.

## Build two timelines

```python
starts = []
ends = []

for start, end in flowers:
    starts.append(start)
    ends.append(end)
```

For:

```python
flowers = [[1, 6], [3, 7], [9, 12], [4, 13]]
```

the lists initially become:

```text
starts = [1, 3, 9, 4]
ends   = [6, 7, 12, 13]
```

We no longer need to keep each start paired with its end. Every query only needs two independent totals: how many starts have occurred and how many ends have already passed.

## Sort both timelines

```python
starts.sort()
ends.sort()
```

```text
starts = [1, 3, 4, 9]
ends   = [6, 7, 12, 13]
```

Sorting allows binary search to count events without scanning every flower for every person.

## Count flowers that started

```python
started = bisect_right(starts, person)
```

`bisect_right` returns the insertion position after all values equal to `person`. Therefore, its index equals the number of starts satisfying:

```text
start <= person
```

For `person = 3`:

```text
starts = [1, 3, | 4, 9]
                 index 2
```

The starts at `1` and `3` both count, so `started = 2`.

## Count flowers that already ended

```python
ended = bisect_left(ends, person)
```

`bisect_left` returns the insertion position before values equal to `person`. Its index equals the number of ends satisfying:

```text
end < person
```

For `person = 7`:

```text
ends = [6, | 7, 12, 13]
            index 1
```

Only the flower ending at `6` has already ended. The flower ending exactly at `7` is still blooming, so `ended = 1`.

## Why different bisect functions?

The bloom interval is inclusive on both sides:

```text
start <= person <= end
```

Therefore:

```python
bisect_right(starts, person)  # Includes start == person
bisect_left(ends, person)     # Excludes end == person from ended count
```

### Memory rule

```text
right on starts → started by now
left on ends    → ended before now
```

## Full dry run

Given:

```python
flowers = [[1, 6], [3, 7], [9, 12], [4, 13]]
people = [2, 3, 7, 11]
```

After sorting:

```text
starts = [1, 3, 4, 9]
ends   = [6, 7, 12, 13]
answer = []
```

### Person at time `2`

```text
started = bisect_right(starts, 2) = 1
ended   = bisect_left(ends, 2)     = 0
blooming = 1 - 0 = 1

answer = [1]
```

### Person at time `3`

```text
started = bisect_right(starts, 3) = 2
ended   = bisect_left(ends, 3)     = 0
blooming = 2 - 0 = 2

answer = [1, 2]
```

### Person at time `7`

```text
started = bisect_right(starts, 7) = 3
ended   = bisect_left(ends, 7)     = 1
blooming = 3 - 1 = 2

answer = [1, 2, 2]
```

### Person at time `11`

```text
started = bisect_right(starts, 11) = 4
ended   = bisect_left(ends, 11)     = 2
blooming = 4 - 2 = 2

answer = [1, 2, 2, 2]
```

## Implementation with comments

```python
from bisect import bisect_left, bisect_right


class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        starts = []
        ends = []

        # Separate every interval into independent start and end timelines.
        for start, end in flowers:
            starts.append(start)
            ends.append(end)

        # Sorting lets us count relevant events with binary search.
        starts.sort()
        ends.sort()

        answer = []

        for person in people:
            # bisect_right counts flowers with start <= person.
            started = bisect_right(starts, person)

            # bisect_left counts flowers with end < person. A flower ending
            # exactly at this time is still blooming because ends are inclusive.
            ended = bisect_left(ends, person)

            # Active flowers are those that started minus those already ended.
            answer.append(started - ended)

        return answer
```

## Complexity

Let `n` be the number of flowers and `m` the number of people.

- Build timelines: `O(n)`
- Sort timelines: `O(n log n)`
- Two binary searches per person: `O(m log n)`
- Total time: `O(n log n + m log n)`
- Extra space: `O(n)`

## Edge cases

- A person arrives exactly when a flower starts: count it.
- A person arrives exactly when a flower ends: count it.
- A person arrives before every flower: answer is `0`.
- A person arrives after every flower: answer is `0`.
- Flower intervals can overlap completely or partially.

## Common mistakes

- Using `bisect_right` for ends and incorrectly removing flowers ending at the query time.
- Forgetting to import `bisect_left` and `bisect_right`.
- Subtracting flowers with `end <= person` instead of only `end < person`.
- Running a full flower scan for every person, producing `O(nm)` time.

## What I learned

For inclusive intervals, count starts at or before the query and subtract ends strictly before it. Separate sorted event timelines make both counts available through binary search.
