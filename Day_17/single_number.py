class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            if i == 0 and num not in nums[i+1:]:
                return num

            elif num not in nums[i+1:] and i != 0 and num not in nums[:i]:
                return num

            elif i == len(nums) and num not in nums[:i]:
                return num

    def singleNumber_one_liner(self, nums):
        return 2 * sum(set(nums)) - sum(nums)


if __name__ == '__main__':

    input = [2,2,1]
    instance = Solution()
    %timeit solution = instance.singleNumber(input)
    %timeit solution2 = instance.singleNumber_one_liner(input)

    print(solution)

[4,1,2,1,2][0+1:]
[4,1,2,1,2][:1]
