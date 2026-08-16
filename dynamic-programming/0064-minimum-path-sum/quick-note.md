# Minimum Path Sum — Quick Revision

- **Pattern:** Grid dynamic programming
- **Recognition clue:** Find a minimum or maximum path value in a grid with restricted movement.
- **State:** `dp[row][col]` is the minimum total cost to reach that cell.
- **Choices:** Reach the current cell from above or from the left.
- **Transition:** `grid[row][col] + min(dp[row - 1][col], dp[row][col - 1])`
- **Base cases:** Start with `grid[0][0]`; initialize the first row from the left and the first column from above.
- **Answer:** `dp[rows - 1][cols - 1]`
- **Time:** `O(rows × cols)`
- **Space:** `O(rows × cols)`, optimizable to `O(cols)`
- **Common mistake:** Forgetting to add the current cell's value or mishandling the first row and column.
- **Memory sentence:** Keep the cheaper journey from above or left, then pay for the current cell.
