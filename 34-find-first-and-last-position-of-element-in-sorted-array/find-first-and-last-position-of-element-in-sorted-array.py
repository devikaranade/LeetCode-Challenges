class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearch(nums, target, is_left):
            index = -1
            l, r = 0, len(nums)-1
            while l<=r:
                mid = (r+l)//2
                if nums[mid]==target:
                    if is_left:
                        r=mid-1
                    else:
                        l = mid+1
                if nums[mid]==target:
                    index = mid 
                elif nums[mid]<target:
                    l+=1
                else:
                    r=mid-1
            return index
        left = binSearch(nums, target, True)
        right = binSearch(nums, target, False) 
        return [left, right]



        