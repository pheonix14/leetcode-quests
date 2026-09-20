# Created by pheonix14 at 2026/09/21 00:35
# leetgo: 1.4.18
# https://leetcode.com/problems/palindrome-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        return str(x) == str(x)[::-1]

# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    ans = Solution().isPalindrome(x)
    print("\noutput:", serialize(ans, "boolean"))
