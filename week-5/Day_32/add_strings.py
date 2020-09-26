class Solution:

    def addStrings(self, num1: str, num2: str) -> str:

        num_1 = self.str_to_int(num1)

        num_2 = self.str_to_int(num2)

        return f'{num_1 + num_2}'

    

    def str_to_int(self, str_nums):

        dict = { '0':0, '1':1,'2':2,'3':3,'4':4, '5':5,'6':6,'7':7,'8':8,'9':9}

​

        str_nums_rev = str_nums[::-1]

        num =0

        for i, str_num in enumerate(str_nums_rev):

            num += dict[str_num] * 10**i

        return num
