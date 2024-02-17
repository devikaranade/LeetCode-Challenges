class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites)==1:
            return True
        graph = {i: [] for i in range(numCourses)} # [[], []]

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        s = set()
        def dfs(course):
            if course in s:
                return False
            if graph[course]==[]:
                return True
            s.add(course)
            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False
            s.remove(course)
            graph[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

