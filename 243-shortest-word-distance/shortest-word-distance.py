class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        p1 = -1
        p2 = -1
        n = len(wordsDict)
        min_dist = n

        for i in range(n):
            if wordsDict[i]==word1:
                p1=i
            if wordsDict[i]==word2:
                p2=i
            if p1!=-1 and p2!=-1:
                min_dist = min(min_dist, abs(p1-p2))
        return min_dist
