class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for c in range(len(s)):
            if s[c]=='(':
                stack.append(0) #
            else:
                pop_bracket = stack.pop()
                if pop_bracket==0:
                    stack[-1] += 1
                else:
                    stack[-1]+=2*pop_bracket

        return stack[0]
        