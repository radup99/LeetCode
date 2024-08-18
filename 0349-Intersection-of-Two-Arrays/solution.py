class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for x in nums1:
            if x in nums2 and x not in intersection:
                intersection.append(x)
        return intersection
