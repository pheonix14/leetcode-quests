# Created by pheonix14 at 2026/09/21 00:29
# leetgo: 1.4.18
# https://leetcode.com/problems/zigzag-conversion/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        rows = [''] * numRows
        curr_row, going_down = 0, False
        for c in s:
            rows[curr_row] += c
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            curr_row += 1 if going_down else -1
        return "".join(rows)

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    numRows: int = deserialize("int", read_line())
    ans = Solution().convert(s, numRows)
    print("\noutput:", serialize(ans, "string"))
