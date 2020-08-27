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

if __name__ == '__main__':

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    instance = Solution()
    solution = instance.intersection(nums1, nums2)

    print(solution)
