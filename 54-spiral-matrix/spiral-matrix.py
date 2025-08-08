class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        up = left = 0
        right = n-1
        down = m-1
        while len(res)<m*n:
            for i in range(left, right+1):
                res.append(matrix[up][i])
            
            for j in range(up+1, down+1):
                res.append(matrix[j][right])
            
            if up!=down:
                for i in range(right-1, left-1, -1):
                    res.append(matrix[down][i]) 
            
            if left!=right:
                for i in range(down-1, up, -1):
                    res.append(matrix[i][left])

            left+=1
            right-=1
            up+=1
            down-=1
        return res

