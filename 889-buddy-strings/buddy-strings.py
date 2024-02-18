class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        count = 0
        if len(s)!=len(goal):
            return False
        if s==goal:
            return len(set(s))<len(s)
        if sorted(s)!=sorted(goal):
            return False
        for i in range(len(s)):
            if s[i]!=goal[i]:
                count+=1
        if count==2 or count==0:
            return True
        else:
            return False

        