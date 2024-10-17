class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # visted = [1,0]
        visited = [0] * numCourses
        G = defaultdict(list)
        for src,des in prerequisites:
            G[des].append(src)

        def dfs(course):
            if visited[course]==1:
                return True
            if visited[course]==2:
                return False
            visited[course]=1
            for neighbor in G[course]:
                if dfs(neighbor):
                    return True
            visited[course]=2
            return False

        
        for c in range(numCourses):
            if dfs(c):
                return False
        return True
 