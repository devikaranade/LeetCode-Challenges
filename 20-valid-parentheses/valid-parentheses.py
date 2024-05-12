class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'{':"}", "(":")", "[":"]"}
        stack = []
        for c in s:
            if c in brackets:
                stack.append(c)
            else:
                if len(stack)==0 or c!=brackets[stack.pop()] :
                    return False
        return len(stack)==0
