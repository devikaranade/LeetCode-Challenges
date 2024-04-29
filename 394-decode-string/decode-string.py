class Solution:
    def decodeString(self, s: str) -> str:
        '''
    
        '''
        stack = []
        curr = ""
        num = 0
        for c in s:
            if c.isdigit():
                num=num*10 + int(c)
            elif c=="[":
                stack.append(num)
                stack.append(curr)
                num=0
                curr=""
            elif c=="]":
                prev=stack.pop()
                prev_num = stack.pop()
                curr=prev+curr*prev_num
            else:
                curr+=c
        return curr