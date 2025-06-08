class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def rec(ip, op):
            if ip=="":
                ans.append(op)
                return ans
            if ip[0].isalpha():
                op1 = op+ip[0].lower()
                op2 = op+ip[0].upper()
                rec(ip[1:], op1)
                rec(ip[1:], op2)
            else:
                rec(ip[1:], op+ip[0])
        rec(s, '')
        return ans