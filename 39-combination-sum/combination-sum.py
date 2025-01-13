class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(remainder, comb, start):
            if remainder==0:
                res.append(list(comb))
                return 
            elif remainder<0:
                return
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remainder-candidates[i],comb, i)
                comb.pop()

        

        backtrack(target, [], 0)
        return res