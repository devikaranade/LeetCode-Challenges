class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {char: i for i, char in enumerate(order)}
        for i in range(1, len(words)):
            word1=words[i-1]
            word2=words[i]
            min_len = min(len(word1), len(word2))
            for j in range(min_len):
                if word1[j]!=word2[j]:
                    if order_map[word1[j]]>order_map[word2[j]]:
                        return False
                    break
            else:
                if len(word1)>len(word2):
                    return False
        return True
