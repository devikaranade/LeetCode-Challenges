class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            k = n-1
            j = i+1
            while j<k:
                tmp = nums[i]+nums[j]+nums[k]
                if tmp==0:
                    s.add((nums[i], nums[j], nums[k]))
                    j+=1
                elif tmp>0:
                    k-=1
                else:
                    j+=1
        return s
