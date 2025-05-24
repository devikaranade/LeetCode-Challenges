class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_freq = 0
        counter = defaultdict(int)
        max_res = 0

        for r in range(len(s)):
            counter[s[r]]+=1
            max_freq = max(max_freq, counter[s[r]])

            while (r-l+1)-max_freq>k:
                counter[s[l]]-=1
                l+=1
            max_res = max(max_res, r-l+1)
        
        return max_res