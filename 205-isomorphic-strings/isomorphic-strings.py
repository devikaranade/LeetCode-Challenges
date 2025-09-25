class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        counter_s_t = Counter()
        counter_t_s = Counter()

        for c1,c2 in zip(s,t):
            if (c1 not in counter_s_t) and (c2 not in counter_t_s):
                counter_s_t[c1]=c2
                counter_t_s[c2]=c1
            elif counter_s_t[c1]!=c2 or counter_t_s[c2]!=c1:
                return False
        return True