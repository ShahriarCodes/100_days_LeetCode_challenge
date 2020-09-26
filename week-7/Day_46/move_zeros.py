class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        hashmap = {}
        count = 0
        for i, num in enumerate(nums):
            # print(i,num)
            if num == 0:
                count += 1
                index = i


        # nums = nums + [0]*c
        return c

#not my solution
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[last] = nums[last], nums[i]
                last += 1
        return nums

if __name__ == '__main__':
    numbers = [0,0,1]

    instance = Solution()
    solution = instance.moveZeroes(numbers)
    print(solution)
