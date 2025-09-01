class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            if not nums:
                return nums
            avg_val = target//k
            if avg_val<nums[0] or nums[-1]<avg_val:
                return res
            if k==2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i==0 or nums[i-1]!=nums[i]:
                    for subset in kSum(nums[i+1:], target-nums[i], k-1):
                        res.append([nums[i]]+subset)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            low, high = 0, len(nums)-1

            while low<high:
                cur_sum = nums[low]+nums[high]
                if cur_sum<target or (low>0 and nums[low]==nums[low-1]):
                    low+=1
                elif cur_sum>target or (high<len(nums)-1 and nums[high]==nums[high+1]):
                    high-=1
                else:
                    res.append([nums[low], nums[high]])
                    low+=1
                    high-=1
            return res

        nums.sort()
        return kSum(nums, target, 4)
            