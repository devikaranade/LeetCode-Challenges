class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        i, j = row-1, 0
        while i>=0 and j<col:
            print(matrix[i][j])
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                j+=1
            else:
                i-=1
        return False


        