class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
                return True
        return False
               
    def containsDuplicate_faster(self,nums):
        return len(set(nums)) == len(nums)


if __name__ == 'main':
    nums = [1,2,1,3]
    instance = Solution()
    print(instance.containsDuplicate(nums))

