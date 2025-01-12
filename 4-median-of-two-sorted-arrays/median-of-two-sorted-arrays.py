class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1+nums2
        merged = sorted(merged)
        print(merged)
        if len(merged)%2!=0:
            val = len(merged)//2
            return merged[val]
        else:
            n1 = len(merged)//2
            print(merged[n1])
            n2 = (len(merged)//2)-1
            print(merged[n2])
            return (merged[n1]+merged[n2])/2
        