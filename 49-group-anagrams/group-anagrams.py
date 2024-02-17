class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            k = str(sorted(i))
            if k not in anagrams:
                anagrams[k] = []
            anagrams[k].append(i)
        return list(anagrams.values())        