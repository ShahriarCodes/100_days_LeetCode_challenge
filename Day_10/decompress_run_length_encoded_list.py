class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_list = []
        range_ = int(len(nums)/2)

        for i in range(range_):
            temp_list = []
            freq = nums[2*i]
            val  =  nums[2*i+1]
            temp_list.append(val)
            new_list = new_list + temp_list*freq

        return new_list


if __name__ == '__main__':

    nums = [1,2,3,4]

    instance = Solution()
    solution = instance.decompressRLElist(nums)
    print(solution)

[]+[1]
