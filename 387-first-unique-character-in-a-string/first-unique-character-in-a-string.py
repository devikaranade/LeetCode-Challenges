class Solution:
    def firstUniqChar(self, s: str) -> int:

        q = deque()
        h = Counter(s)
        count = 0
        for c in range(len(s)):
            q.append(s[c])
            if h[q[0]]>1:
                while len(q)>0 and h[q[0]]>1:
                    q.popleft()
                    count+=1
            else:
                return count
        return -1








        