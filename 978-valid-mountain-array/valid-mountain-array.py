class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        i = 0
        j = len(arr)-1
        while i<j:
            if arr[i]<arr[i+1] and arr[j]<arr[j-1]:
                j-=1
                i+=1
            elif arr[i]<arr[i+1]:
                i+=1
            elif arr[j]<arr[j-1]:
                j-=1
            else:
                return False
        if i==j and j!=len(arr)-1 and i!=0:
            return True
        else:
            return False

        
        