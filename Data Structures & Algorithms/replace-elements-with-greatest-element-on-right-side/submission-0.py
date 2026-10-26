class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        
        for i, num in enumerate(arr):
            if i == len(arr) - 1:
                res.append(-1)
            else:
                remaining = sorted(arr[i+1:])
                res.append(remaining[-1])
        return res

        