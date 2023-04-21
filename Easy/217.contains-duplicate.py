#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        return False
        
# @lc code=end

