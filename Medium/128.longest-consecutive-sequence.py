#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        sequence = 1
        for i in nums:
            if i - 1 not in nums:
                cur = i
                cur_sequence = 1
                while cur + 1 in nums:
                    cur += 1
                    cur_sequence += 1
                sequence = max(sequence, cur_sequence)
        return sequence
        

"""
Results:
Runtimes: 299ms, 97.57%
Memory: 29MB, 24.12&
"""


        
# @lc code=end

