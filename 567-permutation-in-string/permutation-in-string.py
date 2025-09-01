class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        c_s1 = Counter(s1)
        c_s2 = Counter()
        l = 0
        r = 1
        for r in range(len(s2)):
            c_s2[s2[r]]+=1
            if r-l+1>len(s1):
                c_s2[s2[l]]-=1
                if c_s2[s2[l]]==0:
                    del c_s2[s2[l]]
                l+=1
            if c_s1==c_s2:
                return True
        return False