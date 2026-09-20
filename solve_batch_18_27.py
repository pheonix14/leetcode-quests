import os
import sys
import glob
import time
import subprocess

problems = {
    18: '''class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums) - 2):
                if j > i+1 and nums[j] == nums[j-1]: continue
                l, r = j+1, len(nums) - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s < target: l += 1
                    elif s > target: r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]: l += 1
                        while l < r and nums[r] == nums[r-1]: r -= 1
                        l += 1; r -= 1
        return res''',
        
    19: '''class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next''',
        
    20: '''class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack''',
        
    21: '''class Solution:
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
        return dummy.next''',
        
    22: '''class Solution:
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
        return res''',
        
    23: '''class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = curr = ListNode()
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next''',
        
    24: '''class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(0, head)
        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            first.next = second.next
            second.next = first
            curr.next = second
            curr = first
        return dummy.next''',
        
    25: '''class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    break
            if not kth:
                break
            groupNext = kth.next
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next''',
        
    26: '''class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1''',
        
    27: '''class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i'''
}

env = os.environ.copy()
env['LEETCODE_SESSION'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiMjMzMTk0NjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhbGxhdXRoLmFjY291bnQuYXV0aF9iYWNrZW5kcy5BdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYTlmMTg3MTE2Mzk3ZjliNzQwMTg3ZjZjM2E2NjUzYzdkMmI4N2Q4MjBlMGZlOGNkNGIwN2ExYzgzNTllNDhmIiwic2Vzc2lvbl91dWlkIjoiOTJjM2FiYzIiLCJpZCI6MjMzMTk0NjQsImVtYWlsIjoicmlzZXJvemUwMHpAcHJvdG9ubWFpbC5jb20iLCJ1c2VybmFtZSI6InBoZW9uaXgxNCIsInVzZXJfc2x1ZyI6InBoZW9uaXgxNCIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9waGVvbml4MTQvYXZhdGFyXzE3ODc0MDg4NDIucG5nIiwicmVmcmVzaGVkX2F0IjoxNzg5OTMwMDAwLCJpcCI6IjE1Mi41OC4xNjIuMTc1IiwiaWRlbnRpdHkiOiI5MjU0MzY4ODRjYzlhNmI4MDA1ZmViMDU1YzYxMGJhZiIsImRldmljZV93aXRoX2lwIjpbImE2Y2FlMjg4YzUyMTQ4MTk4ODRkMWFiNGExNGRjOTE1IiwiMTUyLjU4LjE2Mi4xNzUiXX0.6RrCTuklHIMdLvKJ1pNXXyuC7TgiJ_39Cuwl0JZ_C8c'
env['LEETCODE_CSRFTOKEN'] = 'hkQbKBVvDb3Ul8HfK1hvmdeaYvnP4gFw'

for qid, code in problems.items():
    print(f"--- Picking {qid} ---")
    subprocess.run([r".\leetgo.exe", "pick", str(qid)], env=env)
    
    search_str = f"python/{qid:04d}.*/solution.py"
    files = glob.glob(search_str)
    if not files:
        print(f"Could not find generated file for {qid}")
        continue
    
    file_path = files[0]
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    start_idx = content.find("class Solution:")
    end_idx = content.find("# @lc code=end")
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + code + "\n\n" + content[end_idx:]
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
    
    print(f"--- Submitting {qid} ---")
    subprocess.run([r".\leetgo.exe", "submit", str(qid)], env=env)
    
    print("Waiting 10 seconds to avoid rate limits...")
    time.sleep(10)
