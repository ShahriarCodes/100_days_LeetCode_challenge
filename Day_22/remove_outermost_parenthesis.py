class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = 0
        new_index = 0
        stack = []

        for index , bracket in enumerate(S):
            if bracket == '(':
                count += 1
            if bracket == ')':
                count -=1
            if count == 0:
                # print (S[new_index:index+1],'\n')
                stack += [S[new_index:index+1]]
                new_index = index + 1

        output = ''
        for elem in stack:
            output += elem[1:-1]
            # print(output)
        return output


if __name__ == '__main__':

    nums = "()()"
    instance = Solution()
    solution = instance.removeOuterParentheses(nums)

    print(solution)
