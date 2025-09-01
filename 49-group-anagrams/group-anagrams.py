class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = defaultdict(list)
        for s in strs:
            sorted_s = tuple(sorted(s))
            anag[sorted_s].append(s)
        res = []
        for v in anag.values():
            res.append(v)
        return res