#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3: return max(nums)
        def rob1(start, end):
            if start >= end: return 0
            dp0 = 0
            dp1 = nums[start]
            for i in range(start+1, end):
                tmp = dp0
                dp0 = max(dp0, dp1)
                dp1 = tmp + nums[i]
            return max(dp0, dp1)
        #print(res, res1)
        return max(rob1(1, n), rob1(0, n-1))
# @lc code=end

