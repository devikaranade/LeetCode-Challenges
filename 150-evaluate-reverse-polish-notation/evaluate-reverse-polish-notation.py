class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in "+-/*":
                stack.append(int(tokens[i]))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if tokens[i]=="+":
                    res = num2+num1
                elif tokens[i]=="-":
                    res = num1-num2
                elif tokens[i]=="*":
                    res = num1*num2
                else:
                    res = int(num1/num2)
                stack.append(res)
        return stack[-1]
