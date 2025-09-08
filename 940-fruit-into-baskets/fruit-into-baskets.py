class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        c = defaultdict(int)
        max_cnt = 0
        while r<len(fruits):
            c[fruits[r]]+=1
            while len(c)>2:
                c[fruits[l]]-=1
                if c[fruits[l]]==0:
                    del c[fruits[l]]
                l+=1
            max_cnt = max(max_cnt, r-l+1)
            r+=1
        return max_cnt
            