#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = len(s)-1
        while i >= 0 and s[i] == " ":
            i-=1
        if i < 0:
            return 0
        j = i
        while j >= 0 and s[j] != ' ':
            j -= 1
        return i - j
        
# @lc code=end

