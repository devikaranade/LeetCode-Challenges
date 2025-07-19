class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1+nums2
        merged = sorted(merged)
        if len(merged)%2!=0:
            val = len(merged)//2
            return merged[val]
        else:
            n1 = len(merged)//2
            n2 = (len(merged)//2)-1
            return (merged[n1]+merged[n2])/2
        