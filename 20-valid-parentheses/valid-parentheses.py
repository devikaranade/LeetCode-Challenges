class Solution:
    def isValid(self, s: str) -> bool:
        br = {
            '(':')',
            '[':']',
            '{':'}'
        }
        stack = []
        for c in s:
            if c in br:
                stack.append(c)
            else:
                if len(stack)==0 or br[stack.pop()]!=c:
                    return False
        return not stack

