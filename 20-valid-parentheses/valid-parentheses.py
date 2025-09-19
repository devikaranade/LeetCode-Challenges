class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')', '[':']', '{':'}'
        }
        stack = []
        for ch in range(len(s)):
            if s[ch] in brackets:
                stack.append(s[ch])
            else:
                if len(stack)==0 or brackets[stack.pop()]!=s[ch]:
                    return False

        return len(stack)==0