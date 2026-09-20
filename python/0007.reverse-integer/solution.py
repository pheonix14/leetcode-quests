# Created by pheonix14 at 2026/09/21 00:29
# leetgo: 1.4.18
# https://leetcode.com/problems/reverse-integer/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31) <= rst <= 2**31 - 1 else 0

# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    ans = Solution().reverse(x)
    print("\noutput:", serialize(ans, "integer"))
