class Solution:
    def checkRecord(self, s: str) -> bool:
        attendance_record = Counter(s)
        if attendance_record['A']<2 and 'LLL' not in s:
            return True
        
        return False