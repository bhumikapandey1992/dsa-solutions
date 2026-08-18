# DSA Solutions and Revision Notes

This repository contains my coding-problem solutions, detailed explanations, and short revision notes.

## How to use this repository

- Read `explanation.md` when learning or revisiting a problem in depth.
- Read `quick-note.md` for fast revision.
- Use `solution.py` to review the final implementation.
- Record personal mistakes and insights; these are especially valuable during revision.

## Problems

| # | Problem | Pattern | Difficulty | Solution | Detailed Explanation | Quick Revision |
|---:|---|---|---|---|---|---|
| 49 | Group Anagrams | Hash Map / Sorting | Medium | [Python](hash-maps/0049-group-anagrams/solution.py) | [Explanation](hash-maps/0049-group-anagrams/explanation.md) | [Quick note](hash-maps/0049-group-anagrams/quick-note.md) |
| 63 | Unique Paths II | Grid DP | Medium | [Python](dynamic-programming/0063-unique-paths-ii/solution.py) | [Explanation](dynamic-programming/0063-unique-paths-ii/explanation.md) | [Quick note](dynamic-programming/0063-unique-paths-ii/quick-note.md) |
| 64 | Minimum Path Sum | Grid DP | Medium | [Python](dynamic-programming/0064-minimum-path-sum/solution.py) | [Explanation](dynamic-programming/0064-minimum-path-sum/explanation.md) | [Quick note](dynamic-programming/0064-minimum-path-sum/quick-note.md) |
| 120 | Triangle | Bottom-up DP | Medium | [Python](dynamic-programming/0120-triangle/solution.py) | [Explanation](dynamic-programming/0120-triangle/explanation.md) | [Quick note](dynamic-programming/0120-triangle/quick-note.md) |
| 767 | Reorganize String | Greedy / Max Heap | Medium | [Python](heaps/0767-reorganize-string/solution.py) | [Explanation](heaps/0767-reorganize-string/explanation.md) | [Quick note](heaps/0767-reorganize-string/quick-note.md) |
| 2357 | Make Array Zero by Subtracting Equal Amounts | Set / Observation | Easy | [Python](arrays/2357-make-array-zero/solution.py) | [Explanation](arrays/2357-make-array-zero/explanation.md) | [Quick note](arrays/2357-make-array-zero/quick-note.md) |

## Folder structure

```text
dsa-solutions/
├── README.md
├── templates/
│   ├── explanation-template.md
│   └── quick-note-template.md
├── arrays/
│   └── 2357-make-array-zero/
│       ├── solution.py
│       ├── explanation.md
│       └── quick-note.md
├── dynamic-programming/
│   ├── 0063-unique-paths-ii/
│   │   ├── solution.py
│   │   ├── explanation.md
│   │   └── quick-note.md
│   ├── 0064-minimum-path-sum/
│   │   ├── solution.py
│   │   ├── explanation.md
│   │   └── quick-note.md
│   └── 0120-triangle/
│       ├── solution.py
│       ├── explanation.md
│       └── quick-note.md
├── hash-maps/
│   └── 0049-group-anagrams/
│       ├── solution.py
│       ├── explanation.md
│       └── quick-note.md
└── heaps/
    └── 0767-reorganize-string/
        ├── solution.py
        ├── explanation.md
        └── quick-note.md
```

## Adding a new problem

1. Choose the most relevant pattern folder, such as `arrays`, `graphs`, or `dynamic-programming`.
2. Create a folder named `number-problem-name`, for example `0001-two-sum`.
3. Add the solution, detailed explanation, and quick note.
4. Add the problem to the table above.
5. Commit the changes with a descriptive message.
