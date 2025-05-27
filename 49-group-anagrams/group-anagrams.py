class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_strs=defaultdict(list)
        res = []
        for s in strs:
            sorted_s = tuple(sorted(s))
            map_strs[sorted_s].append(s)
        for v in map_strs.values():
            res.append(v)
        return res
