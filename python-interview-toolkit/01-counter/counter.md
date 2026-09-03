# `collections.Counter`

## What it is

`Counter` is a dictionary designed for frequency counting. Its keys are the
items being counted and its values are their counts. Unlike a regular dictionary,
reading a missing key returns `0`.

```python
from collections import Counter

counts = Counter("banana")

print(counts)                  # Counter({'a': 3, 'n': 2, 'b': 1})
print(counts["a"])            # 3
print(counts["z"])            # 0
print(counts.most_common(2))   # [('a', 3), ('n', 2)]
```

Building a counter takes `O(n)` time and up to `O(k)` space, where `k` is the
number of distinct items. A count lookup is `O(1)` on average.

## What it can do

### Update frequencies

```python
inventory = Counter(apples=2)
inventory.update(["apples", "pears"])
# Counter({'apples': 3, 'pears': 1})
```

### Treat collections as multisets

Duplicates matter in a multiset. Counter subtraction discards zero and negative
results, which makes it useful for finding missing items.

```python
needed = Counter("aabc")
available = Counter("aaabbcd")

missing = needed - available  # Counter()
can_build = not missing       # True
shared = needed & available   # Counter({'a': 2, 'b': 1, 'c': 1})
```

### Find frequent values

```python
counts = Counter([4, 4, 1, 4, 1, 3])
top_two = counts.most_common(2)  # [(4, 3), (1, 2)]
```

For equal counts, `most_common` uses first-seen order. If a problem specifies a
different tie-breaker, implement that rule explicitly.

## When to recognize it

Reach for `Counter` when a prompt mentions frequencies, occurrences, anagrams,
permutations, duplicates, most-common values, or constructing one collection
from another. Use a set only when the number of duplicates does not matter.

