# Created by pheonix14 at 2026/09/21 00:37
# leetgo: 1.4.18
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
                   '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = ['']
        for d in digits:
            res = [prefix + char for prefix in res for char in mapping[d]]
        return res

# @lc code=end

if __name__ == "__main__":
    digits: str = deserialize("str", read_line())
    ans = Solution().letterCombinations(digits)
    print("\noutput:", serialize(ans, "string[]"))
