#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        return [i[0] for i in sorted(dic.items(), key=lambda x: x[1], reverse=True)[:k]]

        
# @lc code=end

