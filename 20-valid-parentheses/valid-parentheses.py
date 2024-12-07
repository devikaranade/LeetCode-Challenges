class Solution:
    def isValid(self, s: str) -> bool:
        brackets = { '(':')', '{':'}', '[':']' }
        stack = []
        for ch in s:
            if ch in brackets: 
                stack.append(ch) 
            else:
                if len(stack)==0 or ch!=brackets[stack.pop()]:
                    return False
        return len(stack)==0