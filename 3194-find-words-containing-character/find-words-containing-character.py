class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        count = 0
        result = []
        for i in range(len(words)):
            if x in words[i]:
                count+=1
                result.append(i)
        return result

        
        