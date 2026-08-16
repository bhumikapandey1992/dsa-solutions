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
