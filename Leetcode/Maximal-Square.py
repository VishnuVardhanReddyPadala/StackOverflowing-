class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0
        
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        
        return max_side * max_side
