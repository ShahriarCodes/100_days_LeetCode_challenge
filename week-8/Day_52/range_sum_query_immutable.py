class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # acc = 0
        # for index in range(i,j+1):
        #     acc += self.nums[index]
        # return acc 
        return sum(self.nums[i:j+1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)


