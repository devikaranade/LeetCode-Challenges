class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num=0
        pre = "+"
        for ch in s+"+":
            if ch.isdigit():
                num=num*10 + int(ch)
            elif ch in "+-*/":
                if pre=="+":
                    stack.append(num)
                elif pre=="-":
                    stack.append(-num)
                elif pre=="*":
                    stack.append(stack.pop()*num)
                elif pre=="/":
                    stack.append(math.trunc(stack.pop()/num))
                pre=ch
                num=0
        return sum(stack)
                



        