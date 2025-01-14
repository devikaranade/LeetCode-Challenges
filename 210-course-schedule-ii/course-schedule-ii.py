class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited = [0]*numCourses

        if numCourses==1:
            return [0]
        
        G = defaultdict(list)
        for src,des in prerequisites:
            G[des].append(src)
        
        def dfs(courses):
            if visited[courses]==1:
                return True
            if visited[courses]==2:
                return False
            visited[courses]=1

            for neighbor in G[courses]:
                if dfs(neighbor):
                    return True
            visited[courses]=2
            res.append(courses)
            return False   

        for c in range(numCourses):
            if dfs(c):
                return []
        return res[::-1]
 