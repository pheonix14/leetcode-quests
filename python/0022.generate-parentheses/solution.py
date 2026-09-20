# Created by pheonix14 at 2026/09/21 00:40
# leetgo: 1.4.18
# https://leetcode.com/problems/generate-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s, left, right):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        backtrack('', 0, 0)
        return res

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().generateParenthesis(n)
    print("\noutput:", serialize(ans, "string[]"))
