#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            prefix = strs[0]
            for i in range(1, len(strs)):
                while strs[i].find(prefix) != 0:
                    prefix = prefix[:-1]
                    if not prefix:
                        return ""
            return prefix
# @lc code=end

