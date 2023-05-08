#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.track = []
        self.track_sum = 0
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        def backtrack(start):
            if self.track_sum == target:
                res.append(self.track)
                return
            if self.track_sum > target:
                return
            for i in range(start, n):
                self.track = self.track + [candidates[i]]
                self.track_sum += candidates[i]
                backtrack(i)
                self.track = self.track[:-1]
                self.track_sum -= candidates[i]
        backtrack(0)
        return res
# @lc code=end

