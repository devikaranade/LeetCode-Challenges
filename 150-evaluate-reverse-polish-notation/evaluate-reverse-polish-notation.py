class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in '+-/*':
                stack.append(int(tokens[i]))
            else:
                nums2 = stack.pop()
                nums1 = stack.pop()
                if tokens[i] == '+':
                    total = nums2 + nums1
                elif tokens[i]=='-':
                    total = nums1 - nums2
                elif tokens[i] == '*':
                    total = nums1 * nums2
                else:
                    
                    total = int(nums1/nums2)
                stack.append(total)
        return stack[-1]


