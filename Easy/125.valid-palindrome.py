#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalpha() and not s[i].isdigit(): 
                i += 1
            while i < j and not s[j].isalpha() and not s[j].isdigit(): 
                j -= 1
            if s[i].lower() != s[j].lower(): 
                return False
            i += 1
            j -= 1
        return True
    
"""
Results:
Runtime: 59ms, 23,56%

Memory Usage: 14.7MB, 65,51%

"""
# @lc code=end

