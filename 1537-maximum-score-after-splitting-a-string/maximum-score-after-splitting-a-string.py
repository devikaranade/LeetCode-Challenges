class Solution:
    def maxScore(self, s: str) -> int:
        left_sum = s[0]
        right_sum = s[1:]
        max_score = left_sum.count('0') + right_sum.count('1')
        # print(max_score)
        for i in range(1, len(s)):
            if len(right_sum)<=1:
                break
            if len(left_sum)>=len(s):
                break
            left_sum+=s[i]
            right_sum = right_sum[1:]
            new_max = left_sum.count('0') + right_sum.count('1')
            if new_max>max_score:
                max_score = new_max
        return max_score


