# 120. Triangle

## Problem in simple words

We are given a triangle of numbers. Starting at the top, move to an adjacent number in the row directly below until reaching the bottom.

From position `(row, col)`, the two allowed children are:

- directly below: `(row + 1, col)`;
- below and to the right: `(row + 1, col + 1)`.

Find the smallest possible sum along a complete top-to-bottom path.

## Example

```text
       2
      3 4
     6 5 7
    4 1 8 3
```

The minimum path is:

```text
2 → 3 → 5 → 1
```

Its total is `2 + 3 + 5 + 1 = 11`.

## The key idea: solve it bottom-up

A top-down solution must keep track of how we reached border positions. Working from the bottom avoids those border checks.

At any cell, there are exactly two valid children beneath it. If we already know the cheapest cost from each child to the bottom, the current answer is simply:

```text
current value + cheaper child
```

We start with the bottom row, where no decision remains, and repeatedly collapse one triangle level upward until only the peak answer remains.

## Full analogy: the mountain-resort checkout

Imagine the triangle is a mountain resort built on several terraces. You begin at the peak and must slide down to the base.

```text
                         PEAK
                          [2]
                        /     \
                     [3]       [4]
                    /   \     /   \
                 [6]    [5]      [7]
                /   \  /   \    /   \
              [4]   [1]   [8]   [3]       BASE
```

Every bracketed number is a rest house:

- the number is the toll charged for entering that house;
- every house looks down at exactly two houses on the next terrace;
- the left ramp leads to the child at the same column;
- the right ramp leads to the child at the next column;
- your goal is to reach the base while paying the smallest total toll.

Standing at the peak and guessing which ramp will eventually be cheapest is difficult. A low toll now can lead to expensive tolls later. Instead, we send a smart traveler to calculate from the base upward.

### The traveler’s clipboard

The traveler carries one clipboard called `dp`:

```text
┌────────┬────────┬────────┬────────┐
│ Slot 0 │ Slot 1 │ Slot 2 │ Slot 3 │
└────────┴────────┴────────┴────────┘
```

Each slot records:

> The cheapest total bill for finishing the journey from this position to the base.

The traveler does not need a clipboard for every terrace. After solving a terrace, the same slots can be erased and reused for the terrace above.

### Step 0: file the base-floor prices

At the base, the journey is already finished. The remaining bill from a base house is simply that house’s own toll.

```text
Base houses:       [4]   [1]   [8]   [3]
                     ↓     ↓     ↓     ↓
Clipboard:         [4]   [1]   [8]   [3]
```

So the initial state is:

```text
dp = [4, 1, 8, 3]
```

### Step 1: climb to the `[6, 5, 7]` terrace

The traveler now stands in front of each house on the terrace above the base. For every house, the clipboard already shows the complete cost of taking either downward ramp.

#### House `6`

```text
             current toll
                  [6]
                 /   \
                v     v
left child      [4]   [1]      right child
                  \   /
                 choose 1

total = 6 + min(4, 1) = 7
```

The right ramp is cheaper. Erase the old `4` in slot `0` and write `7`:

```text
dp = [7, 1, 8, 3]
      ^
    updated
```

#### House `5`

```text
                  [5]
                 /   \
                v     v
               [1]   [8]
                 \   /
                choose 1

total = 5 + min(1, 8) = 6
```

Update slot `1`:

```text
dp = [7, 6, 8, 3]
         ^
       updated
```

#### House `7`

```text
                  [7]
                 /   \
                v     v
               [8]   [3]
                 \   /
                choose 3

total = 7 + min(8, 3) = 10
```

Update slot `2`:

```text
dp = [7, 6, 10, 3]
             ^
           updated
```

The final `3` is now dead history. The terrace being summarized contains only three houses, so only the useful prefix `[7, 6, 10]` matters.

```text
Solved terrace:       [6]     [5]     [7]
                        \       \       \
Cheapest totals:       [7]     [6]     [10]

Useful clipboard:     [ 7,      6,      10 ]   (3 ignored)
```

### Step 2: climb to the `[3, 4]` terrace

The clipboard no longer represents individual base-house prices. It now contains the cheapest complete bill from each house on the `[6, 5, 7]` terrace to the base.

#### House `3`

```text
                  [3]
                 /   \
                v     v
               [7]   [6]      cheapest solved totals below
                 \   /
                choose 6

total = 3 + min(7, 6) = 9
```

```text
dp = [9, 6, 10, 3]
      ^
    updated
```

#### House `4`

```text
                  [4]
                 /   \
                v     v
               [6]   [10]
                 \   /
                choose 6

total = 4 + min(6, 10) = 10
```

```text
dp = [9, 10, 10, 3]
         ^
       updated
```

Only `[9, 10]` remains meaningful. The other clipboard slots belong to lower terraces that have already been compressed.

### Step 3: land on the peak `[2]`

At the peak, the traveler looks at the final two possible journeys:

```text
                         [2]
                        /   \
                       v     v
                      [9]   [10]
                        \   /
                       choose 9

                 2 + min(9, 10) = 11
```

The traveler erases slot `0` one final time and writes `11`:

```text
dp = [11, 10, 10, 3]
      ^
  final peak
```

The program returns `dp[0]`, which is the cheapest possible resort bill: `11`.

### Watch the mountain melt upward

The full calculation can be viewed as the triangle collapsing into a single answer:

```text
Original mountain          Cheapest totals after each collapse

       [2]                              [11]
      [3, 4]             →             [9, 10]
    [6, 5, 7]                       [7, 6, 10]
  [4, 1, 8, 3]                   [4, 1, 8, 3]
```

Or as the traveler’s clipboard getting shorter:

```text
Floor filed:             [ 4,  1,  8,  3 ]
                              ↓
One terrace higher:        [ 7,  6, 10 ]
                              ↓
One terrace higher:          [ 9, 10 ]
                              ↓
Peak solved:                   [11]
```

### Why the analogy matches the code

| Code | Mountain-resort meaning |
|---|---|
| `triangle[row][col]` | The toll charged by the current rest house |
| `dp` | The traveler’s reusable clipboard of cheapest remaining bills |
| `dp[col]` | The solved bill through the left ramp |
| `dp[col + 1]` | The solved bill through the right ramp |
| `min(dp[col], dp[col + 1])` | Choose the cheaper downward route |
| `triangle[row][col] + ...` | Add the current house’s toll to that route |
| `return dp[0]` | Read the final cheapest bill written at the peak |

The clipboard saves memory because it reuses one row of notes. The unused slots are not physically deleted; each higher terrace simply looks at a shorter prefix of the same array.

## DP state

During the calculation for `(row, col)`:

- `dp[col]` is the cheapest total beginning at its left child `(row + 1, col)`;
- `dp[col + 1]` is the cheapest total beginning at its right child `(row + 1, col + 1)`.

After updating `dp[col]`, it becomes the cheapest total beginning at the current cell.

## Transition

```python
dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
```

In words:

```text
cheapest total from current cell
= current cell's value
+ cheaper of its two children
```

## Why the DP array begins as a copy

```python
dp = list(triangle[-1])
```

The last row is the base case. From a bottom-row cell, the cheapest remaining path contains only that cell, so its value is already the correct answer.

Using `list(...)` creates a separate array. Updating `dp` therefore does not modify the input triangle.

## Why the loops move backward

```python
for row in range(len(triangle) - 2, -1, -1):
```

The loop starts at the second-to-last row because the last row is already stored in `dp`. It stops after processing row `0`, the peak.

For a triangle with four rows, the row indexes are processed in this order:

```text
2, 1, 0
```

The inner loop visits every cell that exists in the current row:

```python
for col in range(len(triangle[row])):
```

## Complete dry run

Start by copying the floor:

```text
dp = [4, 1, 8, 3]
```

### Process row `[6, 5, 7]`

For `6`:

```text
6 + min(4, 1) = 7
dp = [7, 1, 8, 3]
```

For `5`:

```text
5 + min(1, 8) = 6
dp = [7, 6, 8, 3]
```

For `7`:

```text
7 + min(8, 3) = 10
dp = [7, 6, 10, 3]
```

The trailing `3` is now old history and will no longer be used.

### Process row `[3, 4]`

For `3`:

```text
3 + min(7, 6) = 9
dp = [9, 6, 10, 3]
```

For `4`:

```text
4 + min(6, 10) = 10
dp = [9, 10, 10, 3]
```

### Process peak `[2]`

```text
2 + min(9, 10) = 11
dp = [11, 10, 10, 3]
```

The final answer is stored at `dp[0]`, so we return `11`.

The useful portion of the clipboard can be visualized as:

```text
[4, 1, 8, 3]
   ↓ collapse
 [7, 6, 10]
   ↓ collapse
   [9, 10]
   ↓ collapse
     [11]
```

## Why left-to-right in-place updates are safe

When calculating position `col`, the code needs the old values at `dp[col]` and `dp[col + 1]`.

- `dp[col]` has not yet been overwritten for the current position.
- `dp[col + 1]` is to the right and has not yet been processed in this row.

After `dp[col]` is updated, the next calculation uses `dp[col + 1]` and `dp[col + 2]`, so it never needs the old `dp[col]` again. This is why a single array works.

## Implementation

```python
class Solution(object):
    def minimumTotal(self, triangle):
        # 1. Initialize our DP array as a copy of the triangle's bottom row
        dp = list(triangle[-1])

        # 2. Travel upward from the second-to-last row up to the peak (row 0)
        for r in range(len(triangle) - 2, -1, -1):
            # 3. Scan across each element in the current row
            for c in range(len(triangle[r])):
                # Current total = today's value + cheapest of the two children beneath us
                dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])

        # 4. The peak cell now holds the absolute minimum path sum
        return dp[0]
```

## Complexity

Let `n` be the total number of cells in the triangle and `h` be the number of rows:

- Time: `O(n)` because each triangle cell above the base is processed once.
- Extra space: `O(h)` because `dp` contains the width of the bottom row.

A full 2D DP table would require `O(n)` extra space. Reusing one row is the main optimization in this solution.

## Common mistakes

- Starting at the top and introducing unnecessary left-edge and right-edge checks.
- Using unrelated children such as `(row + 1, col - 1)`.
- Forgetting that the valid children are at indexes `col` and `col + 1`.
- Updating the input triangle accidentally instead of copying the bottom row.
- Iterating the rows downward instead of from the second-to-last row upward.
- Returning the entire array instead of `dp[0]`.
- Describing this as a greedy algorithm. Each choice uses already-solved optimal subproblems, so this is dynamic programming.

## What I learned

When a structure narrows toward one final state, try solving from the wide base toward the narrow peak. The triangle then collapses naturally, border cases disappear, and a full 2D table can become one reusable row.
