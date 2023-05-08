#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp0 = 0
        dp1 = nums[0]
        for i in range(1, len(nums)):
            tmp = dp0
            dp0 = max(dp0, dp1)
            dp1 = tmp + nums[i]
        return max(dp0, dp1)
# @lc code=end

