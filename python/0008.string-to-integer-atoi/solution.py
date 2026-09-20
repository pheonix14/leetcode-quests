# Created by pheonix14 at 2026/09/21 00:35
# leetgo: 1.4.18
# https://leetcode.com/problems/string-to-integer-atoi/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s: return 0
        sign = 1
        if s[0] in ['+', '-']:
            if s[0] == '-': sign = -1
            s = s[1:]
        res = 0
        for c in s:
            if not c.isdigit(): break
            res = res * 10 + int(c)
        res *= sign
        return min(max(res, -2**31), 2**31 - 1)

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().myAtoi(s)
    print("\noutput:", serialize(ans, "integer"))
