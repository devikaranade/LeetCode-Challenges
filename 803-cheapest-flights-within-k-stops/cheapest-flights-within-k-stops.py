class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        map_ = defaultdict(list)
        visited = [float('inf')] * n
        visited[src]=0
        

        for flight in flights:
            map_[flight[0]].append((flight[1], flight[2]))
        q = deque([(src,0)]) # [(0,0)]
        k+=1 # k=2
        while k>0 and q:
            size = len(q)
            while size>0:
                curr_node, curr_price = q.popleft()
                for adj, price in map_[curr_node]:
                    new_price = curr_price + price
                    if new_price < visited[adj]:
                        visited[adj]=new_price
                        q.append((adj, new_price))
                size-=1
            k-=1
        return visited[dst] if visited[dst]!=float('inf') else -1
 