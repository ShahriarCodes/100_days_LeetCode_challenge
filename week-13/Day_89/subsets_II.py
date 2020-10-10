class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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
        
        #sorting items in powerset:
        for i in range(len(power_set)):
            power_set[i] = sorted(power_set[i])
        
        #removing duplicates
        final = []
        for i in range(len(power_set)):
            if power_set[i] not in final:
                final.append(power_set[i])
        return final

