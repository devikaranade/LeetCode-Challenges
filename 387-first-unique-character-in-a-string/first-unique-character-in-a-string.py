class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        q = deque()
        count = 0
        for c in range(len(s)):
            q.append(s[c])
            if freq[s[c]]>1:
                while len(q)>0 and freq[s[c]]>1:
                    q.popleft()
                    count+=1
            else:
                return count
        return -1