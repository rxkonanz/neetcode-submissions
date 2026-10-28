class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        result = []
        for index, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                result.append(index)
                result.append(seen[difference])
            else:
                seen[num] = index
        return sorted(result)