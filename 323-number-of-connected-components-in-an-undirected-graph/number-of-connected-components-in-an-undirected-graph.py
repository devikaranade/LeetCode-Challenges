class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        q = deque()
        count = 0
        connections = defaultdict(list)
        seen = set()
        for src, dst in edges:
            connections[src].append(dst)
            connections[dst].append(src)

        for i in range(n):
            if i in seen:
                continue
            q.append(i)
            while q:
                node = q.popleft()
                if node in seen:
                    continue
                seen.add(node)
                for neighbor in connections[node]:
                    q.append(neighbor)
            count+=1
        return count
                