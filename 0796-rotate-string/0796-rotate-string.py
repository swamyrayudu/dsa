class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s1 = len(s)
        s2 = len(goal)
        if s1 != s2:
            return False
        connect = s + s
        if goal in connect:
            return True
        else:
            return False
