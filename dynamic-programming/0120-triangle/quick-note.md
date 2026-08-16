# Triangle — Quick Revision

- **Pattern:** Bottom-up dynamic programming with 1D space optimization
- **Recognition clue:** Move through adjacent cells in a triangle and minimize the complete path sum.
- **Direction:** Begin at the bottom row and collapse upward to the peak.
- **State:** `dp[col]` stores the cheapest total from that position to the bottom.
- **Children:** From `(row, col)`, use `(row + 1, col)` and `(row + 1, col + 1)`.
- **Transition:** `dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])`
- **Base case:** Copy the bottom row into `dp`.
- **Answer:** `dp[0]`
- **Time:** `O(total cells)`
- **Extra space:** `O(number of rows)`
- **Common mistake:** Processing top-down and creating avoidable border cases, or using the wrong child indexes.
- **Memory sentence:** Copy the floor, choose the cheaper two children, and melt the triangle upward until only the peak remains.
