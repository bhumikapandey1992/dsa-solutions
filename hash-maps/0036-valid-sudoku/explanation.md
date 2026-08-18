# 36. Valid Sudoku

## Problem in simple words

Determine whether the filled cells of a 9×9 Sudoku board obey these rules:

1. A digit cannot repeat in the same row.
2. A digit cannot repeat in the same column.
3. A digit cannot repeat in the same 3×3 box.

Empty cells are represented by `"."` and are ignored.

The board does not need to be complete or solvable. We only validate the digits already present.

## The key observation

Every filled cell belongs to exactly three regions:

```text
one row + one column + one 3×3 box
```

When we encounter a digit, ask:

```text
Have I already seen this digit in its row?
Have I already seen this digit in its column?
Have I already seen this digit in its box?
```

If any answer is yes, the board is invalid. Otherwise, record the digit in all three regions.

## Full analogy: three security checkpoints

Imagine every filled Sudoku cell is a passenger carrying a digit badge. Each passenger must pass three security checkpoints:

- the row checkpoint;
- the column checkpoint;
- the 3×3-box checkpoint.

Each checkpoint keeps a set of badges it has already admitted.

```text
Cell (row, column)
        │
        ├──→ Row set
        ├──→ Column set
        └──→ Box set
```

Suppose cell `(0, 1)` contains `5`:

```text
rows[0]       receives "5"
columns[1]    receives "5"
boxes[0]      receives "5"
```

If another `5` later arrives at any of those same checkpoints, that checkpoint rejects it and we return `False`.

## The three collections

We create nine sets for every region type:

```python
rows = [set() for _ in range(9)]
columns = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]
```

Visualized:

```text
rows:       [R0, R1, R2, R3, R4, R5, R6, R7, R8]
columns:    [C0, C1, C2, C3, C4, C5, C6, C7, C8]
boxes:      [B0, B1, B2, B3, B4, B5, B6, B7, B8]
```

Each set contains the digits already seen in that region.

## Understanding the 3×3 box logic from scratch

The board contains 81 individual cell coordinates:

```text
row = 0 through 8
column = 0 through 8
```

We need to compress those 81 coordinates into only nine box identities.

The easiest way to understand this is in two stages:

1. Convert the cell into a two-coordinate box address such as `(0, 1)`.
2. Convert that box address into one flat box index such as `1`.

Do not start by memorizing the final formula. Understand the two-coordinate address first.

### Stage 1: integer division creates three groups

Python integer division discards the remainder:

```text
0 // 3 = 0
1 // 3 = 0
2 // 3 = 0

3 // 3 = 1
4 // 3 = 1
5 // 3 = 1

6 // 3 = 2
7 // 3 = 2
8 // 3 = 2
```

This is exactly the grouping Sudoku needs. Every three consecutive indexes collapse into one group:

```text
Actual index:      0  1  2 | 3  4  5 | 6  7  8
After index // 3:  0  0  0 | 1  1  1 | 2  2  2
```

For rows:

```text
rows 0, 1, 2 → box-row 0
rows 3, 4, 5 → box-row 1
rows 6, 7, 8 → box-row 2
```

For columns:

```text
columns 0, 1, 2 → box-column 0
columns 3, 4, 5 → box-column 1
columns 6, 7, 8 → box-column 2
```

Therefore, a cell’s two-coordinate box address is:

```python
(row // 3, column // 3)
```

### The complete box-coordinate map

```text
                    columns 0–2       columns 3–5       columns 6–8
                    column // 3 = 0    column // 3 = 1    column // 3 = 2

                  ┌──────────────────┬──────────────────┬──────────────────┐
rows 0–2          │                  │                  │                  │
row // 3 = 0      │    Box (0, 0)    │    Box (0, 1)    │    Box (0, 2)    │
                  │                  │                  │                  │
                  ├──────────────────┼──────────────────┼──────────────────┤
rows 3–5          │                  │                  │                  │
row // 3 = 1      │    Box (1, 0)    │    Box (1, 1)    │    Box (1, 2)    │
                  │                  │                  │                  │
                  ├──────────────────┼──────────────────┼──────────────────┤
rows 6–8          │                  │                  │                  │
row // 3 = 2      │    Box (2, 0)    │    Box (2, 1)    │    Box (2, 2)    │
                  │                  │                  │                  │
                  └──────────────────┴──────────────────┴──────────────────┘
```

### Trace a real cell using the coordinate address

Where does cell `(row=1, column=5)` belong?

```text
box row    = 1 // 3 = 0
box column = 5 // 3 = 1

box address = (0, 1)
```

That is the top-middle box, exactly as the map shows.

### Why every cell in one box gets the same address

Consider the bottom-right box, containing rows `6, 7, 8` and columns `6, 7, 8`.

Top-left corner of that box, cell `(6, 6)`:

```text
(6 // 3, 6 // 3) = (2, 2)
```

Center, cell `(7, 7)`:

```text
(7 // 3, 7 // 3) = (2, 2)
```

Bottom-right corner, cell `(8, 8)`:

```text
(8 // 3, 8 // 3) = (2, 2)
```

All nine cells in that 3×3 region become `(2, 2)`. They are roommates sharing the same box address.

This is the heart of the box logic:

> Dividing both coordinates by `3` removes the exact position inside a box and keeps only which box owns the cell.

## Stage 2: flatten the box address into indexes 0–8

The coordinate address is already sufficient. We could use `(row // 3, column // 3)` as a dictionary key.

This solution instead stores nine box sets in a list:

```python
boxes = [set() for _ in range(9)]
```

A list needs one integer index, so we label the boxes from left to right and top to bottom:

```text
┌─────────┬─────────┬─────────┐
│  Box 0  │  Box 1  │  Box 2  │
├─────────┼─────────┼─────────┤
│  Box 3  │  Box 4  │  Box 5  │
├─────────┼─────────┼─────────┤
│  Box 6  │  Box 7  │  Box 8  │
└─────────┴─────────┴─────────┘
```

The flattening formula is:

```python
box = (row // 3) * 3 + (column // 3)
```

It converts:

```text
(box row, box column) → flat box index
```

### Why multiply the box row by 3?

`row // 3` identifies the horizontal band:

```text
top band:     row // 3 = 0
middle band:  row // 3 = 1
bottom band:  row // 3 = 2
```

Each complete band contains three boxes. Multiplying by `3` skips past all boxes in earlier bands and lands at the first box of the correct band:

```text
top band starts at:     0 * 3 = Box 0
middle band starts at:  1 * 3 = Box 3
bottom band starts at:  2 * 3 = Box 6
```

Think of it as a row skipper:

```text
box row 0 ──skip 0 boxes──→ starts at 0
box row 1 ──skip 3 boxes──→ starts at 3
box row 2 ──skip 6 boxes──→ starts at 6
```

### Why add `column // 3`?

After reaching the correct band, `column // 3` moves sideways within that band:

```text
left box:    column // 3 = 0 → move 0 boxes right
middle box:  column // 3 = 1 → move 1 box right
right box:   column // 3 = 2 → move 2 boxes right
```

So the complete mental model is:

```text
(box row * number of boxes per row) + box column

= skip to the correct horizontal band
  + move right to the correct box
```

### Flatten every coordinate address

```text
Box address    Calculation      Flat index
------------------------------------------------
(0, 0)         0 * 3 + 0            0
(0, 1)         0 * 3 + 1            1
(0, 2)         0 * 3 + 2            2

(1, 0)         1 * 3 + 0            3
(1, 1)         1 * 3 + 1            4
(1, 2)         1 * 3 + 2            5

(2, 0)         2 * 3 + 0            6
(2, 1)         2 * 3 + 1            7
(2, 2)         2 * 3 + 2            8
```

### Trace the PDF example: cell `(4, 7)`

```text
1. Find box row:     4 // 3 = 1
2. Skip to its band: 1 * 3  = 3
3. Find box column:  7 // 3 = 2
4. Move right:       3 + 2  = 5

Cell (4, 7) belongs to Box 5.
```

Visual confirmation:

```text
┌─────────┬─────────┬─────────┐
│  Box 0  │  Box 1  │  Box 2  │
├─────────┼─────────┼─────────┤
│  Box 3  │  Box 4  │ BOX 5 ← │  row 4, column 7
├─────────┼─────────┼─────────┤
│  Box 6  │  Box 7  │  Box 8  │
└─────────┴─────────┴─────────┘
```

### More examples

Cell `(1, 7)`:

```text
(1 // 3) * 3 + (7 // 3)
= 0 * 3 + 2
= Box 2
```

Cell `(4, 5)`:

```text
(4 // 3) * 3 + (5 // 3)
= 1 * 3 + 1
= Box 4
```

Cell `(8, 1)`:

```text
(8 // 3) * 3 + (1 // 3)
= 2 * 3 + 0
= Box 6
```

### The one sentence to remember

```text
row // 3 chooses the box row,
column // 3 chooses the box column,
and box_row * 3 + box_column flattens them into one list index.
```

## Visual dry run

Consider the first row:

```text
["5", "3", ".", ".", "7", ".", ".", ".", "."]
```

### Cell `(0, 0)` contains `5`

```text
row set:     rows[0]     = {}
column set:  columns[0]  = {}
box set:     boxes[0]    = {}
```

No duplicate exists, so add `5`:

```text
rows[0]     = {"5"}
columns[0]  = {"5"}
boxes[0]    = {"5"}
```

### Cell `(0, 1)` contains `3`

`3` is absent from `rows[0]`, `columns[1]`, and `boxes[0]`, so record it:

```text
rows[0]     = {"3", "5"}
columns[1]  = {"3"}
boxes[0]    = {"3", "5"}
```

### Cell `(0, 2)` contains `.`

Skip it. Empty cells do not enter any set.

### What detects an invalid board?

Suppose another `5` appears at `(0, 8)`:

```text
value = "5"
"5" in rows[0] → True
```

The duplicate row value is detected immediately, so return `False`.

Even if its column and box were clear, failing one of the three checks is enough.

## Implementation

```python
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 1. Create one set for every row, column, and 3x3 box
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # 2. Visit every cell in the board
        for row in range(9):
            for column in range(9):
                value = board[row][column]

                # Empty cells do not affect validity
                if value == ".":
                    continue

                # Convert the cell's position into one of the nine box indexes
                box = (row // 3) * 3 + (column // 3)

                # A repeated value in any of its three regions makes the board invalid
                if (
                    value in rows[row]
                    or value in columns[column]
                    or value in boxes[box]
                ):
                    return False

                # Record the value in its row, column, and box
                rows[row].add(value)
                columns[column].add(value)
                boxes[box].add(value)

        return True
```

## Line-by-line mental model

```python
rows = [set() for _ in range(9)]
```

Create nine row checkpoints. Repeat for columns and boxes.

```python
value = board[row][column]
```

Read the current cell.

```python
if value == ".":
    continue
```

Ignore empty cells.

```python
box = (row // 3) * 3 + (column // 3)
```

Determine which 3×3 box owns the cell.

```python
if value in rows[row] or value in columns[column] or value in boxes[box]:
    return False
```

Reject a digit already seen in any of its three regions.

```python
rows[row].add(value)
columns[column].add(value)
boxes[box].add(value)
```

Record a safe digit at all three checkpoints.

## Why a set is the right structure

We need to answer “Have I seen this digit before?” Sets provide average `O(1)` membership checks and automatically keep unique values.

We do not need counts. The first repetition is enough to prove invalidity.

## Complexity

The board always contains 81 cells:

- Time: `O(81)`, conventionally written as `O(1)` because the board size is fixed.
- Extra space: `O(81)`, also `O(1)` for a fixed 9×9 board.

If generalized to an `n × n` board, the scan would take `O(n²)` time and the tracking structures would use `O(n²)` space.

## Common mistakes

- Treating `"."` as a digit and reporting repeated empty cells.
- Checking only rows and columns but forgetting 3×3 boxes.
- Using `(row // 3, column // 3)` inconsistently instead of a stable box identifier.
- Adding a value before checking for duplication, which would always find itself.
- Checking whether the puzzle can be solved; this problem asks only whether current entries are valid.
- Comparing strings as integers unnecessarily; string digits work correctly in sets.

## What I learned

When every item belongs to several independent uniqueness regions, maintain one set per region and validate all of an item’s memberships during a single scan.
