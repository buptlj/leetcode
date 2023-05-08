#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.track = []
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        def backtrack(start):
            res.append(self.track)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                self.track = self.track + [nums[i]]
                backtrack(i+1)
                self.track = self.track[:-1]
        backtrack(0)
        return res
# @lc code=end

