class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        set_len = 2**len(nums)
        power_set = []
        sub_set = []
        for i in range(set_len):
            binary = bin(i)[2:]
            binary = '0'*(len(nums)-len(binary)) + binary
            # print(binary)
            for index, elem in enumerate(binary):
                if elem == '1':
                    sub_set.append(nums[index])
            power_set.append(sub_set)
            sub_set = []
        return power_set 
