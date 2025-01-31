class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = 99999
        for i in range(n-2):
            k = n-1
            j = i+1
            while j<k:
                tmp_sum = nums[i]+nums[j]+nums[k]
                if tmp_sum==target:
                    return tmp_sum
                
                if abs(target-tmp_sum)<abs(target-closest):
                    closest = tmp_sum
                if tmp_sum<target:
                    j+=1
                else:
                    k-=1
                    
    
        return closest