class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            freq[word]=freq.get(word,0)+1
        tuples = [(word,f) for word,f in freq.items()]
        tuples.sort(key=lambda x: (-x[1], x[0]))

        return [t[0] for t in tuples[:k]]