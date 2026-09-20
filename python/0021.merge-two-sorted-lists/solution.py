# Created by pheonix14 at 2026/09/21 00:39
# leetgo: 1.4.18
# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return dummy.next

# @lc code=end

if __name__ == "__main__":
    list1: ListNode = deserialize("ListNode", read_line())
    list2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().mergeTwoLists(list1, list2)
    print("\noutput:", serialize(ans, "ListNode"))
