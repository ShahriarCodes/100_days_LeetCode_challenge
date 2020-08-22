class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = bin(num)[2:]
        complement = ''
        for i in binary:
            if i == '1':
                complement += '0'
            else:
                complement += '1'
        return int(complement,2)

if __name__ == '__main__':

    nums =  1
    instance = Solution()
    solution = instance.findComplement(nums)

    print(solution)

bin(5)
