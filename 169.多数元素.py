#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # res = {}
        # for i in nums:
        #     cnt = res.get(i, 0)
        #     cnt += 1
        #     res[i] = cnt
        # for k, v in res.items():
        #     if v > int(len(nums)/2):
        #         return k
        winner = nums[0]
        cnt  = 1
        for i in nums[1:]:
            if cnt == 0:
                winner = i
                cnt += 1
            else:
                if i == winner:
                    cnt += 1
                else:
                    cnt -= 1
        return winner
        
# @lc code=end

