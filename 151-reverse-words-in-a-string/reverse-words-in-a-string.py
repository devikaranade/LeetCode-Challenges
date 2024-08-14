class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        tmp = []
        for i in s:
            if i!='':
                tmp.append(i)
        return ' '.join(tmp[::-1])