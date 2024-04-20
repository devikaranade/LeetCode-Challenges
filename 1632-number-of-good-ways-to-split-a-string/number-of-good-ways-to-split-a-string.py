class Solution:
    def numSplits(self, s: str) -> int:
        if len(s)==1:
            return 0
        if len(s)==2:
            return 1
        count=0
        left = defaultdict(int)
        right = Counter(s) 
        for c in s:
            left[c]+=1 
            right[c]-=1 
            if right[c]==0:
                right.pop(c) 
            if len(left)==len(right):
                count+=1 
        return count


        # for c in range(1, len(s)):
        #     left = s[:c]
        #     right = s[c:]
        #     # print(left, right)
        #     left_counter = Counter(left)
        #     right_counter = Counter(right)
        #     if len(left_counter)==len(right_counter):
        #         count+=1
        # return count