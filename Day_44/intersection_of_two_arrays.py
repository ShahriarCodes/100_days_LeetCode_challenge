class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        subset = []
        for num in nums1:
            if num in nums2 and num not in subset:
                subset.append(num)
        return subset
