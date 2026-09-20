# Created by pheonix14 at 2026/09/21 00:28
# leetgo: 1.4.18
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = max_len = 0
        for right, c in enumerate(s):
            if c in char_map and char_map[c] >= left:
                left = char_map[c] + 1
            char_map[c] = right
            max_len = max(max_len, right - left + 1)
        return max_len

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().lengthOfLongestSubstring(s)
    print("\noutput:", serialize(ans, "integer"))
