import os
import sys
import glob
import time
import subprocess

problems = {
    3: '''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = max_len = 0
        for right, c in enumerate(s):
            if c in char_map and char_map[c] >= left:
                left = char_map[c] + 1
            char_map[c] = right
            max_len = max(max_len, right - left + 1)
        return max_len''',
    4: '''class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return float(max(maxLeftX, maxLeftY))
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1
        return 0.0''',
    5: '''class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end+1]
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1''',
    6: '''class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        rows = [''] * numRows
        curr_row, going_down = 0, False
        for c in s:
            rows[curr_row] += c
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            curr_row += 1 if going_down else -1
        return "".join(rows)''',
    7: '''class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31) <= rst <= 2**31 - 1 else 0'''
}

env = os.environ.copy()
env['LEETCODE_SESSION'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiMjMzMTk0NjQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhbGxhdXRoLmFjY291bnQuYXV0aF9iYWNrZW5kcy5BdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwYTlmMTg3MTE2Mzk3ZjliNzQwMTg3ZjZjM2E2NjUzYzdkMmI4N2Q4MjBlMGZlOGNkNGIwN2ExYzgzNTllNDhmIiwic2Vzc2lvbl91dWlkIjoiOTJjM2FiYzIiLCJpZCI6MjMzMTk0NjQsImVtYWlsIjoicmlzZXJvemUwMHpAcHJvdG9ubWFpbC5jb20iLCJ1c2VybmFtZSI6InBoZW9uaXgxNCIsInVzZXJfc2x1ZyI6InBoZW9uaXgxNCIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9waGVvbml4MTQvYXZhdGFyXzE3ODc0MDg4NDIucG5nIiwicmVmcmVzaGVkX2F0IjoxNzg5OTMwMDAwLCJpcCI6IjE1Mi41OC4xNjIuMTc1IiwiaWRlbnRpdHkiOiI5MjU0MzY4ODRjYzlhNmI4MDA1ZmViMDU1YzYxMGJhZiIsImRldmljZV93aXRoX2lwIjpbImE2Y2FlMjg4YzUyMTQ4MTk4ODRkMWFiNGExNGRjOTE1IiwiMTUyLjU4LjE2Mi4xNzUiXX0.6RrCTuklHIMdLvKJ1pNXXyuC7TgiJ_39Cuwl0JZ_C8c'
env['LEETCODE_CSRFTOKEN'] = 'hkQbKBVvDb3Ul8HfK1hvmdeaYvnP4gFw'

for qid, code in problems.items():
    print(f"--- Picking {qid} ---")
    subprocess.run([r".\leetgo.exe", "pick", str(qid)], env=env)
    
    # Find the python file
    search_str = f"python/{qid:04d}.*/solution.py"
    files = glob.glob(search_str)
    if not files:
        print(f"Could not find generated file for {qid}")
        continue
    
    file_path = files[0]
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace everything from class Solution: to # @lc code=end
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
