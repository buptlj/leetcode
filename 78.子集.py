#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, tmp):
            #print(tmp)
            res.append(tmp)
            for i in range(start, len(nums)):
                backtrack(i+1, tmp + [nums[i]])
        backtrack(0, [])
        return res
# @lc code=end

