#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or nums[0] > target or nums[-1] < target: 
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            #print(left, right, mid)
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        #print(left, right)
        if nums[left] == target:
            res_left = left 
        else:
            res_left = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[right] == target:
            res_right = right
        else:
            res_right = -1
        return [res_left, res_right]


# @lc code=end

