class Solution:
    def minScoreTriangulation(self, values):
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n): 
            for i in range(n - length):
                j = i + length
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    score = dp[i][k] + dp[k][j] + values[i] * values[j] * values[k]
                    dp[i][j] = min(dp[i][j], score)
        
        return dp[0][n - 1]
print(Solution().minScoreTriangulation([1, 2, 3]))        
print(Solution().minScoreTriangulation([3, 7, 4, 5]))     
print(Solution().minScoreTriangulation([1, 3, 1, 4, 1, 5]))
