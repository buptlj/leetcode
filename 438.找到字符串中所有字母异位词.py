#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = {}
        window = {}
        for c in p:
            tmp = need.setdefault(c, 0) + 1
            need[c] = tmp
            window[c] = 0
        left, right = 0, 0
        valid = 0
        res = []
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            #print(left, right, valid, window)
            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)
                c = s[left]
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
            #print('after', left, right, window)
        return res
# @lc code=end

