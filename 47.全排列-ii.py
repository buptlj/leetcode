#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.track = []
        self.used = []
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        self.used = [0] * n
        nums = sorted(nums)
        def backtrack():
            if len(self.track) == n:
                res.append(self.track)
                return
            for i in range(n):
                if self.used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not self.used[i-1]:
                    continue
                self.track = self.track + [nums[i]]
                self.used[i] = 1
                backtrack()
                self.track = self.track[:-1]
                self.used[i] = 0
        backtrack()
        return res

# @lc code=end

