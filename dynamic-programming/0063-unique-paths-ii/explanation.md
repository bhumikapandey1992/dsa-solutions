# 63. Unique Paths II

## Problem in simple words

A robot starts in the top-left corner of a grid and wants to reach the bottom-right corner. It may move only right or down.

Some cells contain obstacles:

- `0` means the cell is open.
- `1` means the cell is blocked.

Count how many different valid paths the robot can take without entering a blocked cell.

## Example

```text
0  0  0
0  1  0
0  0  0
```

The center cell is blocked, so the robot has two valid paths:

```text
Right → Right → Down → Down
Down → Down → Right → Right
```

The answer is `2`.

## Intuition

Imagine each open cell as a room. To enter a room, the robot must arrive either from the room directly above or from the room directly to the left.

Therefore, the number of ways to reach an open cell is:

```text
ways from above + ways from left
```

An obstacle is a locked room. No path can enter it, so the number of ways to reach it is always zero.

## Pattern

This is a grid dynamic-programming problem because:

- the answer for each cell depends on previously calculated neighboring cells;
- movement is restricted to right and down;
- the problem asks us to count paths rather than list them.

## DP state

`dp[row][col]` means:

> The number of valid ways to reach cell `(row, col)` from the top-left without crossing an obstacle.

The DP matrix stores path counts. It does not store the obstacle values themselves.

## Transition

If the current cell is blocked:

```python
dp[row][col] = 0
```

If the current cell is open:

```python
dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
```

In words:

```text
paths to current cell
= paths arriving from above
+ paths arriving from the left
```

## Base cases and borders

### Blocked start or destination

If the starting or ending cell is blocked, no complete path can exist:

```python
if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
    return 0
```

### Starting cell

When the starting cell is open, there is exactly one way to be there: start there.

```python
dp[0][0] = 1
```

### First row

Cells in the first row can only receive paths from the left. If an obstacle appears, that cell remains zero, and every later cell also receives zero from its left until another route becomes possible—which cannot happen within the first row.

### First column

Cells in the first column can only receive paths from above. An obstacle blocks all cells below it from being reached through that column.

## Building the table

For the example:

```text
Obstacle grid       Path-count DP table

0  0  0             1  1  1
0  1  0      →      1  0  1
0  0  0             1  1  2
```

Notice the center entry:

- it is an obstacle, so its path count is `0`;
- the bottom-right cell receives one path from above and one from the left;
- therefore, its value is `1 + 1 = 2`.

## Implementation

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # Calculate grid dimensions explicitly
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        # 1. Edge Case: If start or finish point is blocked, 0 paths can exist
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
            return 0

        # 2. Create a 2D calculations matrix matching our grid size
        dp = [[0] * cols for _ in range(rows)]

        # 3. Base Case: The robot's spawn point has exactly 1 way to exist
        dp[0][0] = 1

        # 4. Fill out the top row border (Row index 0, scanning across columns)
        for c in range(1, cols):
            if obstacleGrid[0][c] == 0:
                # If safe, copy the path count from the left cell
                dp[0][c] = dp[0][c - 1]

        # 5. Fill out the left column border (Column index 0, descending down rows)
        for r in range(1, rows):
            if obstacleGrid[r][0] == 0:
                # If safe, copy the path count from the cell directly above
                dp[r][0] = dp[r - 1][0]

        # 6. Fill the inside of the grid using nested loops
        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0  # Roadblock blocks all incoming traffic!
                else:
                    # New ways = ways from above + ways from left
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        # Return the value stored in the final bottom-right corner room
        return dp[rows - 1][cols - 1]
```

## Why leaving obstacle cells at zero works

The DP matrix begins filled with zeroes. During border initialization, a cell is updated only when it is safe. Therefore, an obstacle remains zero automatically.

Inside the grid, the code explicitly assigns zero to an obstacle. Neighboring cells may then include that zero in their addition, which correctly contributes no paths through the blocked cell.

## Complexity

For a grid containing `rows × cols` cells:

- Time: `O(rows × cols)` because every cell is processed once.
- Space: `O(rows × cols)` for the DP matrix.

The space can later be optimized to `O(cols)`, but the 2D matrix makes the path-counting process easier to visualize.

## Connection to related problems

### Unique Paths

Without obstacles, every cell uses the same addition:

```python
dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
```

Unique Paths II adds one rule: a blocked cell must contribute zero paths.

### Minimum Path Sum

Both problems inspect the cells above and to the left, but the operation reflects the question:

```python
# Count all valid routes
above + left

# Select the cheapest route
current_cost + min(above, left)
```

## Common mistakes

- Returning `1` when the starting cell or destination is blocked.
- Treating an obstacle as a path instead of assigning it zero paths.
- Using `min` instead of addition; this problem counts all valid paths.
- Resetting the first-row or first-column count to `1` after an obstacle.
- Allowing diagonal movement even though only right and down are permitted.
- Forgetting that `dp[row][col]` stores a number of paths, not a distance.

## What I learned

For counting problems, combine independent ways using addition. Obstacles do not require a new recurrence; they simply force the path count at that state to zero.
