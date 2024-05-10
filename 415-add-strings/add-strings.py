class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1==0:
            return num2
        if num2==0:
            return num1
        r1 = len(num1)-1
        r2 = len(num2)-1
        res = []
        carry = 0
        while r2>=0 or r1>=0 or carry:
            t1 = int(num1[r1]) if r1>=0 else 0
            t2 = int(num2[r2]) if r2>=0 else 0
            total = (t1+t2+carry)%10
            carry = (t1+t2+carry)//10
            res.append(total)
            r1-=1
            r2-=1
        if carry:
            res.append(carry)
        return ''.join(str(x) for x in res[::-1])


            


        
