class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        evenList = []
        odd_List = []
        for num in A:
            if num == 0:
                evenList.append(num)
                print(num)
            elif num%2 ==0:
                evenList.append(num)
            else:
                odd_List.append(num)
        return evenList + odd_List

if __name__ == '__main__':

    A = [0,2,1]
    # A = [0,1,2,3,4,5,69,8]
    instance = Solution()
    solution = instance.sortArrayByParity(A)

    print(solution)
