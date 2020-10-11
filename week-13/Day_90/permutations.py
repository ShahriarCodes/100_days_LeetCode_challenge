class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        else:
            l = []
            for i in range(len(nums)):
                x = nums[i]
                xs = nums[:i] + nums[i+1:]
                for p in self.permute(xs):
                    l.append([x]+p)
            return l
