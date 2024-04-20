class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        # xx:yy -> 00<xx<24 and 00<yy<60
        # 12:34, 13:24, 14:23,14:32.... #23.41
        max_time = -1
        for h, i ,j ,k in itertools.permutations(arr):
            hour = h*10+i #12
            minute = j*10+k
            if hour<24 and minute<60:
                max_time = max(max_time, hour*60 + minute)
        if max_time==-1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time//60, max_time%60)
            

