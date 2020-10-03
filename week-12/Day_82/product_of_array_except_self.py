class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums) 
        forward_pass = [1]* length 
        for i in range(1,length):
            forward_pass[i] = forward_pass[i-1] * nums[i-1]
            
        backward_pass = [1]*len(nums)
        for i in reversed(range(length-1)):
            backward_pass[i] = backward_pass[i+1] *nums[i+1]
        
        print(forward_pass, backward_pass)
        for i in range(length):
            forward_pass[i]  = forward_pass[i] * backward_pass[i]
        return forward_pass
