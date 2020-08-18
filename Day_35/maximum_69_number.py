class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = str(num)
        lst =  []
        for i in range(len(str_num)):
            new_num = str_num
            if str_num[i] == 9:
                new_num[i] = 6
                lst.append(new_num)

            elif str_num[i] == 6:
                new_num[i] = 9
                lst.append(new_num)
        return max(lst)

if __name__ == '__main__':

    num = 9699
    instance = Solution()
    solution = instance.maximum69Number(S)

    print(solution)
