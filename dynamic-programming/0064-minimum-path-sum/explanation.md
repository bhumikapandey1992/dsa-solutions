# 64. Minimum Path Sum

## Problem in simple words

Given a grid of non-negative numbers, start at the top-left and reach the bottom-right. We may move only right or down. Find the smallest possible sum of the cells on the path, including the starting and ending cells.

Think of every cell as a toll booth. The number in the cell is the price paid when stepping on it. We want the cheapest journey across the grid.

## Example

```text
1  3  1
1  5  1
4  2  1
```

The cheapest path has a total cost of `7`:

```text
1 → 3 → 1
        ↓
        1
        ↓
        1
```

## Intuition

To arrive at a cell, we must have come from one of two places:

- the cell directly above it;
- the cell directly to its left.

If we already know the cheapest cost of reaching both of those cells, we choose the cheaper route and then add the value of the current cell.

This works because every path to the current cell must end with one of those two moves.

## DP state

`dp[row][col]` means:

> The minimum total cost required to reach cell `(row, col)` from the top-left.

It represents an accumulated path cost, not the value of that individual grid cell.

## Transition

For a normal cell, we choose the cheaper predecessor and pay the current cell's cost:

```python
dp[row][col] = grid[row][col] + min(
    dp[row - 1][col],
    dp[row][col - 1],
)
```

In words:

```text
cost to reach current cell
= current cell's cost
+ cheaper cost from above or left
```

## Base cases

### Starting cell

There is no choice at the top-left because the journey begins there:

```python
dp[0][0] = grid[0][0]
```

### First row

A cell in the first row has no cell above it, so it can only be reached from the left:

```python
dp[0][col] = dp[0][col - 1] + grid[0][col]
```

### First column

A cell in the first column has no cell to its left, so it can only be reached from above:

```python
dp[row][0] = dp[row - 1][0] + grid[row][0]
```

## Building the table

For the example grid, the DP table develops as follows:

```text
Original grid       Minimum costs

1  3  1             1  4  5
1  5  1      →      2  7  6
4  2  1             6  8  7
```

For example, consider the center cell with value `5`:

- minimum cost from above: `4`;
- minimum cost from the left: `2`;
- choose `2` and add the current cost `5`;
- therefore, `dp[1][1] = 7`.

The bottom-right entry contains the final answer: `7`.

## Implementation

```python
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]

        # First row
        for col in range(1, cols):
            dp[0][col] = dp[0][col - 1] + grid[0][col]

        # First column
        for row in range(1, rows):
            dp[row][0] = dp[row - 1][0] + grid[row][0]

        # Remaining cells
        for row in range(1, rows):
            for col in range(1, cols):
                dp[row][col] = grid[row][col] + min(
                    dp[row - 1][col],
                    dp[row][col - 1],
                )

        return dp[rows - 1][cols - 1]
```

## Complexity

For a grid with `rows × cols` cells:

- Time: `O(rows × cols)` because every cell is processed once.
- Space: `O(rows × cols)` for the DP table.

The space can later be optimized to `O(cols)`, but the 2D version makes the idea easier to understand.

## Connection to Unique Paths

Both problems use information from above and left:

```python
# Unique Paths: count both possibilities
dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

# Minimum Path Sum: choose the cheaper possibility
dp[row][col] = grid[row][col] + min(
    dp[row - 1][col],
    dp[row][col - 1],
)
```

The grid movement is the same. The operation changes according to what the problem asks us to calculate.

## Common mistakes

- Forgetting to include the current cell's value.
- Treating `dp[row][col]` as the cell's own cost instead of the accumulated path cost.
- Using a diagonal predecessor even though diagonal movement is not allowed.
- Applying the normal transition to the first row or column without handling boundaries.
- Forgetting that the starting cell is included in the path sum.

## What I learned

When movements are restricted, reverse the question. Instead of asking, “Where can I go from here?”, ask, “Where could I have come from?” That often reveals the DP transition.
