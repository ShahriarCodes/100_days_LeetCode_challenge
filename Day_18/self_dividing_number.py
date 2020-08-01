class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        #creating an empty list to be returned
        nums = []
        #iterating through every number from left to right
        for num in range(left, right+1):
            #initializing remainder
            remainder = 0
            #saving the number into a new variable to compute
            new_num = num
            #initializing j to check if number is divisible by the digits or not
            j = 0
            #total number of digits
            len_num = len(str(num))
            #iterating till the number gets divided by every digits(from last to first)
            for i in range(len_num):
                #remainder(every last digit in each iteration
                remainder = new_num % 10
                #check if remainder passes the cases below
                if remainder != 0 and num % remainder == 0:
                    #renew the new_num by truncating by 10
                    new_num = new_num // 10
                    #increment j as a counter to compare later
                    j += 1

                else:
                    #renew j as 0 if the previous case does not pass
                    j = 0
                    #and brak the loop as the current number is not divisible by its digits
                    break
            #check if j is greater than zero as a reminder of the number being divisible
            if j > 0:
                # concatenate current number into the list
                nums += [num]
        return nums


if __name__ == '__main__':

    left = 1
    right = 22
    instance = Solution()
    solution = instance.selfDividingNumbers(left, right)

    print(solution)


num = 22
remainder = 0
new_num = num
j = 0
for i in range(len(str(num))):
    remainder = new_num % 10
    if num % remainder == 0:
        new_num = new_num // 10
        j += 1

    else:
        j= 0
        break
