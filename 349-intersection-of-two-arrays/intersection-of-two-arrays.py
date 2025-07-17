class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()
        nums1.sort()
        nums2.sort()
        m = len(nums1)
        n = len(nums2)
        l = 0
        r = 0
        while l<m and r<n:
            if nums1[l]==nums2[r]:
                s.add(nums1[l])
                l+=1
                r+=1
            elif nums1[l]<nums2[r]:
                l+=1
            else:
                r+=1
        return list(s)