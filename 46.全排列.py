#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute1(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        if len(nums) == 1: return [nums]
        res = []
        for i in range(len(nums)):
            if i == len(nums) - 1:
                data = nums[:i]
            else:
                data = nums[:i]+nums[i+1:]
            tmp = self.permute(data)
            for re in tmp:
                res.append([nums[i]] + re)
        return res
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        if len(nums) == 1: return [nums]
        res = []
        used = [0] * len(nums)
        def backtrack(nums, tmp):
            if len(tmp) == len(nums):
                res.append(tmp)
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = 1
                backtrack(nums, tmp + [nums[i]])
                used[i] = 0
        backtrack(nums, [])
        return res


# @lc code=end

