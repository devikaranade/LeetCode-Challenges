class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1]*n
        for i in range(2*n):
            curr = nums[i%n]
            while stack and nums[stack[-1]]<curr:
                num = stack.pop()
                res[num]=curr
            if i<n:
                stack.append(i)
        return res

            
