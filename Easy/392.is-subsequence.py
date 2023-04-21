#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        i = 0
        for c in t:
            if c == s[i]:
                i += 1
                if i == len(s):
                    return True
        return False
        
# @lc code=end

