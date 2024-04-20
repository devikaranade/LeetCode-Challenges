class Solution:
    def lengthLongestPath(self, input: str) -> int:
        if len(input)<2:
            return 0
        path = {0:0}
        dist = 0
        directory = input.split("\n")
        for line in directory:
            l = line.lstrip("\t")
            depth = len(line)-len(l)
            if '.' in line:
                dist = max(dist, path[depth]+len(l))
            else:
                path[depth+1]=path[depth] + len(l)+1 
        return dist




        