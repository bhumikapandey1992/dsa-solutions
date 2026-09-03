# Lesson 1: `collections.Counter`

## Mental model

A `Counter` is a dictionary whose keys are items and whose values are counts.
Missing keys return `0`, which often removes branching from frequency problems.

```python
from collections import Counter

counts = Counter("banana")
# Counter({'a': 3, 'n': 2, 'b': 1})
```

Building the counter takes `O(n)` time and up to `O(k)` space, where `k` is the
number of distinct values. Looking up one count is `O(1)` on average.

## Operations to know

- `Counter(iterable)`: count values from an iterable.
- `counts[item]`: read a count; a missing item produces `0`.
- `counts.most_common(k)`: get the `k` most frequent `(item, count)` pairs.
- `counts.update(iterable)`: add counts.
- `counts.subtract(iterable)`: subtract counts; zero and negative values remain.
- `counts.elements()`: expand positive counts back into repeated values.
- `a + b`, `a - b`, `a & b`, `a | b`: combine counters as multisets.

To test whether one counter supplies another across Python versions, use
`not (needed - available)`: subtraction keeps only missing positive counts.

`most_common(k)` resolves equal counts by first-seen order. If an interview
problem requires another tie-breaker, encode it explicitly instead of relying on
that behavior.

## Interview recognition cues

Consider a `Counter` when a problem says:

- frequency, occurrence, duplicate, or most common;
- permutation or anagram;
- construct one collection from another;
- compare two collections while respecting duplicates.

A set is insufficient when duplicate counts matter. A normal dictionary can do
the same job, but `Counter` is clearer when values represent frequencies.

## Practice sequence

1. Predict and run `examples.py`.
2. Implement `exercises.py` in order.
3. Run `python3 -m unittest -v test_exercises.py`.
4. Explain the complexity of each solution aloud.
5. Add your observations below and commit your work.

## My notes

- Add surprises, mistakes, and recognition cues here while practicing.
