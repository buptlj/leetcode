
class Solution:
    def threeSum(self, nums):
        def two_sum(nums, target):
            print(nums, target)
            n = len(nums)
            left, right = 0, n - 1
            res = []
            while left < right:
                if nums[left] + nums[right] < target:
                    while left + 1 <= right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                elif nums[left] + nums[right] > target:
                    while right -1 >= left and nums[right - 1] == nums[right]:
                        right -= 1
                    right -= 1
                else:
                    res.append([nums[left], nums[right]])
                    while left + 1 <= right and nums[left] == nums[left + 1]:
                        left += 1
                    while right -1 >= left and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1

            return res
        n = len(nums)
        nums = sorted(nums)
        print(nums)
        res = []
        for i in range(n - 2):
            if nums[i] > 0: continue
            if i > 0 and nums[i] == nums[i-1]: continue
            tmp = two_sum(nums[i+1:], -nums[i])
            tmp = [[nums[i]]+l for l in tmp]
            res.extend(tmp)
        return res

a = [-1,0,1,2,-1,-4]
a = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
solution = Solution()
print(solution.threeSum(a))


