class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = set()
        seen = set()
        for i in range(len(s)-9):
            curr_window = s[i:i+10]
            if curr_window in seen:
                result.add(curr_window)
            else:
                seen.add(curr_window)
        return list(result)
         