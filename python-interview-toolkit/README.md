# Python Interview Toolkit

This track builds fluency with Python's interview-friendly standard library and
language features. Work through the lessons in order. Every lesson stays small:

- `topic.md`: what the tool does, its complexity, and short examples;
- `problem.py`: one representative problem with a runnable implementation;
- `similar-problems.md`: follow-up exercises and related LeetCode questions.

## Study loop

1. Read the concept file and predict each snippet's result.
2. Study the representative problem, then recreate it without looking.
3. Run `python3 problem.py` and explain the complexity aloud.
4. Solve selected questions from `similar-problems.md` in the existing pattern
   folders.
5. Commit each completed problem with its explanation and quick note.

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

The first commit for a lesson adds its three teaching files. Each later practice
commit should contain a completed problem, explanation, and quick note. This
makes the history show both what you studied and how you applied it.
