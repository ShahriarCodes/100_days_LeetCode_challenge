class Solution:
    def numberOfSteps (self, num: int) -> int:

        count = 0
        for i in range(num):
            if num != 0:

                if num %2 == 0:
                    print(f'{num} is even; divide by 2 and obtain {num/2}')
                    num /= 2

                else:
                    print(f'{num} is odd; subtract 1 and obtain {num - 1}')
                    num -= 1
                    

                count+= 1

            else:
                break

        return count
