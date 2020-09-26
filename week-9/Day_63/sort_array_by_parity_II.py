class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        final = []
        odd_stack = []
        even_stack = []
        for i in range(len(A)):
            if A[i] %2 == 0:
                even_stack.append(A[i])
            elif A[i]%2 != 0:
                odd_stack.append(A[i])
        for odd, even in zip(odd_stack, even_stack):
            final.append(even)
            final.append(odd)
        return final
            
