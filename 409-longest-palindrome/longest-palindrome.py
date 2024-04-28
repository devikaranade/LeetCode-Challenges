class Solution:
    def longestPalindrome(self, s: str) -> int:
        total = 0
        k =1
        if not s:
            return 
        if len(s)==1:
            return 1
        map_s = Counter(s)
        print(map_s)
        for c in map_s:
            if map_s[c]%2==0:
                total+=map_s[c]
            if map_s[c]%2!=0:
                if k==1:
                    total+=map_s[c]
                    k=0
                else:
                    total+=map_s[c]-1
        return total
        