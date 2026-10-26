class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        maxNum = 0
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                res.insert(0, -1)
                maxNum = arr[i]
            else:
                res.insert(0, maxNum)
                if arr[i] > maxNum:
                    maxNum = arr[i]
        return res


        