# Unique Paths II — Quick Revision

- **Pattern:** Grid dynamic programming
- **Recognition clue:** Count paths in a grid with right/down movement and blocked cells.
- **State:** `dp[row][col]` is the number of valid ways to reach that cell.
- **Open-cell transition:** `dp[row][col] = dp[row - 1][col] + dp[row][col - 1]`
- **Obstacle transition:** `dp[row][col] = 0`
- **Base case:** If the start or destination is blocked, return `0`; otherwise set `dp[0][0] = 1`.
- **Borders:** The first row copies from the left; the first column copies from above. Obstacles remain zero and block later border cells.
- **Answer:** `dp[rows - 1][cols - 1]`
- **Time:** `O(rows × cols)`
- **Space:** `O(rows × cols)`, optimizable to `O(cols)`
- **Common mistake:** Resetting border cells to `1` after an obstacle or using `min` instead of addition.
- **Memory sentence:** An open room receives every path from above and left; a blocked room receives none.
