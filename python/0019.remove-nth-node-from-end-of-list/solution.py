# Created by pheonix14 at 2026/09/21 00:39
# leetgo: 1.4.18
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().removeNthFromEnd(head, n)
    print("\noutput:", serialize(ans, "ListNode"))
