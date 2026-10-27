class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreboard = []

        for op in operations:
            if op == "+":
                scoreboard.append(scoreboard[-1] + scoreboard[-2])
            elif op == "D":
                scoreboard.append(scoreboard[-1] * 2)
            elif op == "C":
                scoreboard.pop()
            else:
                scoreboard.append(int(op))
        return sum(scoreboard)