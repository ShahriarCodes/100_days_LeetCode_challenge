class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        c = 0
        for num in hashmap:
            if hashmap[num] > c:
                c += hashmap[num]
                answer = num
        return answer
