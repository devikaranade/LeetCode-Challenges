class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [1]
        final = [res]
        if numRows<1:
            return []
        for i in range(1, numRows):
            prev_row = final[i-1]
            curr_row = [1]
            for j in range(1,i):
                curr_row.append(prev_row[j-1]+prev_row[j])
            curr_row.append(1)
            final.append(curr_row)
        return final 