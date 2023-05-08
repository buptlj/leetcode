#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def max_profit_inf(prices):
            dp_i_0 = 0
            dp_i_1 = -float('inf')
            for i in range(len(prices)):
                tmp = dp_i_0
                dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
                dp_i_1 = max(dp_i_1, tmp - prices[i])
            return dp_i_0
        n = len(prices)
        if k > n / 2: return max_profit_inf(prices)
        dp = [[[0] * 2 for i in range(k + 1)] for i in range(n)]
        for i in range(n):
            for j in range(1, k + 1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[-1][k][0]
# @lc code=end

