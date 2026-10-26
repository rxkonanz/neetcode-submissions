class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        newNums = []
        for num in nums:
            if num != val:
                newNums.append(num)
        nums[:] = newNums
        return len(newNums)