class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seen = set()
        G = defaultdict(list)

        for src, des in edges:
            G[src].append(des)
            G[des].append(src)

        def dfs(node):
            seen.add(node)
            if node==destination:
                return True
            for neighbor in G[node]:
                if neighbor not in seen:
                    if dfs(neighbor):
                        return True
            return False
        
        return dfs(source)


        