# Python Interview Toolkit

This track builds fluency with Python's interview-friendly standard library and
language features. Work through the lessons in order. Each lesson contains a
concept note, runnable examples, exercises, and tests.

## Study loop

1. Read the lesson's `README.md` and predict each example's output.
2. Run `python3 examples.py` and explain the time complexity aloud.
3. Implement the functions in `exercises.py` without copying the examples.
4. Run `python3 -m unittest test_exercises.py` from the lesson directory.
5. Record mistakes and insights in the lesson's **My notes** section.
6. Commit the completed lesson with `git commit -am "Practice <topic>"`.

Do not move on until the tests pass and you can explain when the tool is better
than a plain list or dictionary.

## Roadmap

| Order | Lesson | Interview application | Status |
|---:|---|---|---|
| 1 | `collections.Counter` | Frequencies, anagrams, top-k preparation | Ready |
| 2 | `collections.deque` | Queues, BFS, sliding windows | Planned |
| 3 | `heapq` | Top-k, merges, shortest paths | Planned |
| 4 | Sets | Membership, deduplication, cycle detection | Planned |
| 5 | `zip`, `enumerate`, unpacking, slicing | Clean and safe iteration | Planned |
| 6 | `bisect_left`, `bisect_right` | Search and insertion boundaries | Planned |
| 7 | `ord`, `chr` | Character indexing and transformations | Planned |
| 8 | Comprehensions and generators | Concise construction and lazy iteration | Planned |
| 9 | Mixed interview drills | Choosing the right tool under pressure | Planned |

## Commit convention

Keep commits small and searchable:

```text
Add Counter lesson scaffold
Practice Counter frequency operations
Solve Counter interview drills
```

The first commit for a lesson may add its teaching material. A practice commit
should contain your exercise implementations and personal notes. This makes the
history show both what you studied and what you learned.

