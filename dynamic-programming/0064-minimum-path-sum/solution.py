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
