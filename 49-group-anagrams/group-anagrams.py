class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        for s in strs:
            sorted_s = tuple(sorted(s))
            h[sorted_s].append(s)
        res = []
        for v in h.values():
            res.append(v)
        return res
