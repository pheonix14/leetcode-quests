import os
import sys
import glob
import time
import subprocess

problems = {
    8: '''class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s: return 0
        sign = 1
        if s[0] in ['+', '-']:
            if s[0] == '-': sign = -1
            s = s[1:]
        res = 0
        for c in s:
            if not c.isdigit(): break
            res = res * 10 + int(c)
        res *= sign
        return min(max(res, -2**31), 2**31 - 1)''',
        
    9: '''class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        return str(x) == str(x)[::-1]''',
        
    10: '''class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)''',
        
    11: '''class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            max_water = max(max_water, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water''',
        
    12: '''class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ""
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman += syb[i]
                num -= val[i]
            i += 1
        return roman''',
        
    13: '''class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res + roman[s[-1]]''',
        
    14: '''class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return shortest[:i]
        return shortest''',
        
    15: '''class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    l += 1; r -= 1
        return res''',
        
    16: '''class Solution:
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
        return res''',
        
    17: '''class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        mapping = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
                   '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = ['']
        for d in digits:
            res = [prefix + char for prefix in res for char in mapping[d]]
        return res'''
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
