#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start

class Solution:
    def dp(self, coins, amount):
        if amount < 0: return -1
        if amount == 0: return 0
        if amount in self.dpt:
            return self.dpt[amount]
        res = inf
        for i in coins:
            tmp = self.dp(coins, amount - i)
            if tmp < 0:
                continue
            res = min(res, tmp + 1)
        if res == inf:
            res = -1
        self.dpt[amount] = res
        return res
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        if amount < 0: return -1
        #self.dpt = {}
        #return self.dp(coins, amount)
        dpt = [amount + 1] * (amount + 1)
        dpt[0] = 0
        for i in range(len(dpt)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dpt[i] = min(dpt[i], dpt[i-coin] + 1)
        if dpt[amount] == amount + 1:
            return -1
        return dpt[amount]
# @lc code=end

