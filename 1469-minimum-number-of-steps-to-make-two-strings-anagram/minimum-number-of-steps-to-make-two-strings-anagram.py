class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = Counter(s)
        t_freq = Counter(t)
        minval = 0
        for k,v in t_freq.items():
            if v > s_freq[k]:
                minval+=(v-s_freq[k])
        return minval    