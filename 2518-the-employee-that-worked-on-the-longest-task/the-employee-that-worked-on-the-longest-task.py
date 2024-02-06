class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        id_ = logs[0][0]
        max_diff = logs[0][1]
        if len(logs)<=2:
            return 0
        for i in range(1, len(logs)):
            diff = logs[i][1]-logs[i-1][1]
            if diff>max_diff:
                max_diff = diff
                id_ = logs[i][0]
            elif diff==max_diff:
                id_ = min(logs[i][0], id_)
            
        return id_
        
        