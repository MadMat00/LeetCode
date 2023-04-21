#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_value = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = max_value
            if temp > max_value:
                max_value = temp
        return arr

            

        
# @lc code=end

