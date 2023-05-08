#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(nums, target):
            n = len(nums)
            left, right = 0, n - 1
            res = []
            while left < right:
                sum = nums[left] + nums[right]
                low = nums[left]
                high = nums[right]
                if sum < target:
                    while left < right and nums[left] == low:
                        left += 1
                elif sum > target:
                    while right > left and nums[right] == high:
                        right -= 1
                else:
                    res.append([low, high])
                    while left < right and nums[left] == low:
                        left += 1
                    while right > left and nums[right] == high:
                        right -= 1
            return res
        n = len(nums)
        nums = sorted(nums)
        res = []
        for i in range(n - 2):
            if nums[i] > 0: continue
            if i > 0 and nums[i] == nums[i-1]: continue
            tmp = two_sum(nums[i+1:], -nums[i])
            tmp = [[nums[i]] + l for l in tmp]
            res.extend(tmp)
        return res
# @lc code=end

