class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
            
        opener = {
            "[": "]",
            "{": "}",
            "(": ")"
        }
        closer = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        running = []
        for char in s:
            if char in opener:
                running.append(char)
            else:
                if len(running) > 0 and running[-1] == closer[char]:
                    running.pop()
                else:
                    return False
        if len(running) == 0:
            return True
        else:
            return False

