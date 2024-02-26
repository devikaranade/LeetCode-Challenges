class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
    
        def dfs(i, j, ct):
            if ct==len(word):
                return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or word[ct]!=board[i][j] or (i,j) in seen:
                return False
            seen.add((i,j))
            res = (
                dfs(i+1, j, ct+1) or 
                dfs(i, j+1, ct+1) or
                dfs(i-1, j, ct+1) or
                dfs(i, j-1, ct+1)
            )

            seen.remove((i,j))
            return res
        
      
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0):
                    return True
        return False