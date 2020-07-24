class Solution(object):
    def binarydigit(self, n):
        binary = ''
        while n > 0:
            binary += str(n%2)
            n //= 2
        return binary[::-1]

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        binary_x = self.binarydigit(x)
        binary_y = self.binarydigit(y)

        len_x = len(binary_x)
        len_y = len(binary_y)

        if len_x > len_y:
            binary_y = (len_x - len_y)* '0' + binary_y

        if len_x < len_y:
            binary_x = (len_y - len_x)* '0' + binary_x

        return binary_x , binary_y





if __name__ == '__main__':

    x = 1
    y = 4
    instance = Solution()
    solution = instance.hammingDistance(x , y)
    print(solution)
