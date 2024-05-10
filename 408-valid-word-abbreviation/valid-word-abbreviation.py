class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l,r = 0, 0
        while l<len(word) and r<len(abbr):
            if word[l]==abbr[r]:
                l+=1
                r+=1
            else:
                if abbr[r].isdigit():
                    if abbr[r]=="0":
                        return False
                    tmp=0
                    while r<len(abbr) and abbr[r].isdigit():
                        tmp=tmp*10 + int(abbr[r])
                        r+=1       
                    l+=tmp
                else:
                    if l>len(word) or word[l]!=abbr[r]:
                        return False
                    l+=1
                    r+=1
        return l==len(word) and r==len(abbr)
                


        