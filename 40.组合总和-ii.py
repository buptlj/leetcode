#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.track = []
        self.track_sum = 0
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        def backtrack(start):
            if self.track_sum > target:
                return
            if self.track_sum == target:
                res.append(self.track)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                self.track = self.track + [candidates[i]]
                self.track_sum += candidates[i]
                backtrack(i+1)
                self.track = self.track[:-1]
                self.track_sum -= candidates[i]
        backtrack(0)
        return res
# @lc code=end

