#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def up(cur, i):
            res = [s for s in cur]
            if res[i] == '9':
                res[i] = '0'
            else:
                res[i] = str(int(res[i]) + 1)
            return ''.join(res)
        def down(cur, i):
            res = [s for s in cur]
            if res[i] == '0':
                res[i] = '9'
            else:
                res[i] = str(int(res[i]) - 1)
            return ''.join(res)
        #q = [['0', '0', '0', '0']]
        q = ['0000']
        res = 0
        visited = {k: 1 for k in deadends}
        while q:
            tmp = []
            for ele in q:
                if ele in visited:
                    continue
                if ele == target:
                    return res
                visited[ele] = 1
                for i in range(4):
                    up_res = up(ele, i)
                    if up_res not in visited:
                        tmp.append(up_res)
                    dn_res = down(ele, i)
                    if dn_res not in visited:
                        tmp.append(dn_res)
            q = tmp
            res += 1
        return -1
# @lc code=end

