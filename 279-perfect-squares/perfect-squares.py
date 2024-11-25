class Solution:
    def numSquares(self, n: int) -> int:
        l = []
        for i in range(1, int(n**0.5)+1):
            l.append(i*i)
        q = {n}
        level = 0
        while q:
            level+=1
            next_q = set()
            for r in q:
                for sq in l:
                    if r==sq:
                        return level
                    elif r<sq:
                        break
                    else:
                        next_q.add(r-sq)
            q=next_q
        return level
        

        