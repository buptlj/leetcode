#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.track = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, n, k):
            if len(self.track) == k:
                res.append(self.track)
                return
            for i in range(start, n-(k-len(self.track))+1):
                self.track = self.track + [i+1]
                backtrack(i+1, n, k)
                self.track = self.track[:-1]
        backtrack(0, n, k)
        return res
# @lc code=end

