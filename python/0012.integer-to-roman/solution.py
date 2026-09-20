# Created by pheonix14 at 2026/09/21 00:36
# leetgo: 1.4.18
# https://leetcode.com/problems/integer-to-roman/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ""
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman += syb[i]
                num -= val[i]
            i += 1
        return roman

# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().intToRoman(num)
    print("\noutput:", serialize(ans, "string"))
