class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """

        new_num =[]
        for num , _index_ in zip(nums, index):
            new_num.insert(_index_, num)
            print(num,_index_)

        return new_num



if __name__ == '__main__':

    nums = [1,2,3,4,0]
    index = [0,1,2,3,0]
    instance = Solution()
    solution = instance.createTargetArray(nums, index)

    print(solution)
