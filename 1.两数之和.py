#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return
        tmp = {}
        for i, n in enumerate(nums):
            tmp.setdefault(n, []).append(i)
            if target - n in tmp:
                if target - n != n:
                    return [tmp[n][0], tmp[target - n][0]]
                if len(tmp[n]) == 1:
                    continue
                return tmp[n][:2]
# @lc code=end

