class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        f, s = edges[0], edges[1]
        return f[0] if f[0] in s else f[1]
         