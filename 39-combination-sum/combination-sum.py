class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(diff, comb, start):
            if diff==0:
                res.append(list(comb))
                return
            if diff<0:
                return
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(diff-candidates[i], comb, i)
                comb.pop()

        backtrack(target, [], 0)
        return res