class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        q = deque([amount])
        seen = set()
        count=0
        while q:
            for _ in range(len(q)):
                curr_amt = q.popleft()
                for coin in coins:   
                    diff_amt = curr_amt - coin
                    if diff_amt>0 and diff_amt not in seen:
                        seen.add(diff_amt)
                        q.append(diff_amt)
                    if diff_amt==0:
                        return count+1
            count+=1
        return -1
