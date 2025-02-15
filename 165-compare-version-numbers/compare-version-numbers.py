class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        left, right = 0, 0
        v1_len = len(v1)
        v2_len = len(v2)
        if v1_len<v2_len:
            for i in range(v2_len-v1_len, v2_len+1):
                v1.append("0")
        else:
            for i in range(v1_len-v2_len, v1_len+1):
                v2.append("0")
             
        while left<len(v1) and right<len(v2):
            if int(v1[left])==int(v2[right]):
                left+=1
                right+=1
            elif int(v1[left])<int(v2[right]):
                return -1
            else:
                return 1
        return 0