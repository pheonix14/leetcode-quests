# Created by pheonix14 at 2026/09/21 00:41
# leetgo: 1.4.18
# https://leetcode.com/problems/remove-element/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    val: int = deserialize("int", read_line())
    ans = Solution().removeElement(nums, val)
    print("\noutput:", serialize(ans, "integer"))
