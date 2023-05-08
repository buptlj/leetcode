#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        windows = {}
        for c in t:
            tmp = need.setdefault(c, 0)
            need[c] = tmp + 1
            windows[c] = 0
        left, right = 0, 0
        n = len(s)
        valid = 0
        start, length = 0, float('inf')
        while right < n:
            c = s[right]
            right += 1
            if c in need:
                windows[c] += 1
                if windows[c] == need[c]:
                    valid += 1
            #print(left, right)
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                c = s[left]
                left += 1
                if c in need:
                    if windows[c] == need[c]:
                        valid -= 1
                    windows[c] -= 1
            #print(left, right, res)
        if length == float('inf'):
            return ''
        return s[start:start+length]

# @lc code=end

