class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)+1!=n:
            return False
        map_edges = defaultdict(list)
        seen = set()

        for i in edges:
            src=i[0]
            dst=i[1]
            map_edges[src].append(dst)
            map_edges[dst].append(src)
        
        q = deque([0])
        while q:
            node = q.popleft()
            seen.add(node)

            for i in map_edges[node]:
                if i not in seen:
                    q.append(i)
        return len(seen)==n

       