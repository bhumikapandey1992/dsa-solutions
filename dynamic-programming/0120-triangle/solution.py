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
