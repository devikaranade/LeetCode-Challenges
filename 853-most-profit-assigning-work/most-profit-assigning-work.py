class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        diffMap = sorted(zip(difficulty,profit))
        worker.sort()
        i, count, max_profit = 0, 0 ,0 
        for w in worker:
            while i<len(worker) and diffMap[i][0]<=w:
                max_profit = max(max_profit, diffMap[i][1])
                i+=1
            count+=max_profit
        return count
        