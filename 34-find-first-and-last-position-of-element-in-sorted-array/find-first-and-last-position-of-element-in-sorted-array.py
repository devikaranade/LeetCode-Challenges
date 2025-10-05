class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bin_search(nums, target, is_left):
            l=0
            r = len(nums)-1
            index = -1
            while l<=r:
                mid = l+(r-l)//2
                if nums[mid]==target:
                    if is_left:
                        r=mid-1
                    else:
                        l=mid+1
                if nums[mid]==target:
                    index = mid
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return index
        left = bin_search(nums, target, True)
        right = bin_search(nums, target, False)
        return [left,right]