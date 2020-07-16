class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        '''

        dict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000 }

        s_list = [(dict.get(char)) for char in s][::-1]
        s_list_sum = sum(s_list)

        new_list = []
        for i, num in enumerate(s_list):
            if i > 0 and i < len(s_list):
                if s_list[i] < s_list[i-1]:
                    num = -1 * num
            new_list.append(num)

        return sum(new_list)
        # return s_list, s_list_sum, new_list

if __name__ == '__main__':

    x = 'MCMXCIV'
    instance = Solution()
    solution = instance.romanToInt(x)
    # print('list: ', solution[0],'sum: ', solution[1] , 'new_list',  solution[2], sum(solution[2]))
    print(solution)
    # print(type(solution))

[1,2][-1]
