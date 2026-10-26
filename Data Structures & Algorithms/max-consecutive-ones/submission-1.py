class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        totalCount = 0
        currCount = 0
        for i, num in enumerate(nums):
            if num == 1:
                currCount += 1
            if num == 0 or i == len(nums) - 1:
                if currCount > totalCount:
                    totalCount = currCount
                currCount = 0
                
        return totalCount