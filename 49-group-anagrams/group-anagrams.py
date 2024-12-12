class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            k = str(sorted(i))
            if k not in d:
                d[k]=[]
            d[k].append(i)
        return list(d.values())
