# Created by pheonix14 at 2026/09/21 00:37
# leetgo: 1.4.18
# https://leetcode.com/problems/3sum-closest/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return res
        return res

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().threeSumClosest(nums, target)
    print("\noutput:", serialize(ans, "integer"))
