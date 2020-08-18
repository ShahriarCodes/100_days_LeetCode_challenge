class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = str(num)
        lst_num = list(str_num)
        new_lst =  []
        for i in range(len(lst_num)):
            new_num = lst_num[:]
            if lst_num[i] == '9':
                new_num[i] = '6'
                new_lst.append(int("".join(new_num)))

            elif lst_num[i] == '6':
                new_num[i] = '9'
                new_lst.append(int("".join(new_num)))

        new_lst.append(num)
        return max(new_lst)

if __name__ == '__main__':

    num = 9669
    instance = Solution()
    solution = instance.maximum69Number(num)

    print(solution)

list("45454")
''.join(['1','2'])
