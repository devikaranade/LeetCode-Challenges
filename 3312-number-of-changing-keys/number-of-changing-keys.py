class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        last = s[0].lower()
        for c in s[1:]:
            if c.lower()!=last:
                changes+=1
                last=c.lower()
        return changes