class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * length
        for start, end, amt in updates:
            ans[start] += amt
            if end < length - 1:
                ans[end + 1] -= amt     
        for i in range(1, length):
            ans[i] += ans[i - 1]
        return ans