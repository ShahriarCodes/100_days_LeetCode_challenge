class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p:
            return True
        if s == '' and p == '':
            return True
        if s == '':
            return False
        if p == '':
            return False

        i = 0
        new_string = []
        for char, expr in zip(s,p):

            print(char, expr)
            if char == expr:
                new_string.append(char)

            elif expr == '*':
                new_string.append(p[i-1])

            elif expr == '.':
                new_string.append(char)

            i += 1
        return new_string




if __name__ == '__main__':

    s = "aa"
    p = "a*"
    instance = Solution()
    solution = instance.isMatch(s, p)

    print(solution)
