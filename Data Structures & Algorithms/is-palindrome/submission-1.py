class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = -1
        palin = []
        
        for char in s:
            if char.isalnum():
                palin.append(char.lower())

        for i, char in enumerate(palin):
            if palin[i] != palin[j]:
                return False
            j -= 1
        return True