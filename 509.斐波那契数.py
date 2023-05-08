#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2:
            return 1
        a = 1
        b = 1
        for i in range(2, n):
            a, b = b, a + b
        return b
# @lc code=end

