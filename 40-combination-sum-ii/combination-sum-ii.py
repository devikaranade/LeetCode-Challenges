class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(ans, temp_list, candidates, total_left, idx):
            if total_left<0:
                return 
            elif total_left==0:
                ans.append(temp_list.copy())
            else:
                for i in range(idx, len(candidates)):
                    if i>idx and candidates[i]==candidates[i-1]:
                        continue
                    if total_left<candidates[i]:
                        break
                    temp_list.append(candidates[i])
                    backtrack(ans, temp_list, candidates, total_left-candidates[i], i+1)
                    temp_list.pop()

        res = []
        candidates.sort()
        backtrack(res, [], candidates, target, 0)
        return res