class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freq = Counter(s1)
        freqs2 = Counter()
        l=0
        r=1
        for r in range(len(s2)):
            freqs2[s2[r]]+=1
            if r-l+1>len(s1):
                freqs2[s2[l]]-=1
                if freqs2[s2[l]]==0:
                    del freqs2[s2[l]]
                l+=1
            if freqs2==freq:
                return True
        return False