# Created by pheonix14 at 2026/09/21 00:40
# leetgo: 1.4.18
# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(0, head)
        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            first.next = second.next
            second.next = first
            curr.next = second
            curr = first
        return dummy.next

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().swapPairs(head)
    print("\noutput:", serialize(ans, "ListNode"))
