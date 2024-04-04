class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':")", '{':"}", "[":"]"}
        stack = []
        i = 0
        while i<len(s):
            if s[i] in brackets: 
                stack.append(s[i])
            else:
                if len(stack)==0 or s[i]!=brackets[stack.pop()]:
                    return False
            i+=1
        return len(stack)==0
                