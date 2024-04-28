class Solution:
    def compress(self, chars: List[str]) -> int:
        l=0
        ans = 0
        while l<len(chars):
            count=0
            letter = chars[l]
            while l<len(chars) and chars[l]==letter:
                l+=1
                count+=1
            chars[ans]=letter
            ans+=1
            if count>1:
                for c in str(count):
                    chars[ans]=c
                    ans+=1
            
        return ans
            



