class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(counter,comb):
            if len(comb)==len(nums):
                res.append(comb.copy())
                return 
            for num in counter:
                if counter[num]>0:
                    comb.append(num)
                    counter[num]-=1
                    backtrack(counter, comb)
                    comb.pop()
                    counter[num]+=1

        
        res = []
        backtrack(Counter(nums), [])
        return res
