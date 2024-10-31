class Solution:
    def findContestMatch(self, n: int) -> str:
        j = n
        i = 1
        pairs = []
        while i<j:
            pairs.append((i,j))
            i+=1
            j-=1

        while len(pairs)>1:
            tmp = []
            while len(pairs)>0:
                front=pairs.pop(0)
                back = pairs.pop()
                tmp.append((front,back))
            pairs=tmp
        return str(pairs[0]).replace(" ","") 
        


