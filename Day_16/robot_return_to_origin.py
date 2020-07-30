class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x_axis = {'R':1, 'L':-1}
        y_axis = {'U':1, 'D':-1,}

        position = [0,0]
        for move in moves:
            if move in x_axis:
                position[0] += x_axis[move]
            if move in y_axis:
                position[1] += y_axis[move]
        print(position)
        if position == [0,0]:
            return True
        else:
            return False




if __name__ == '__main__':

    input = "ULRD"
    instance = Solution()
    solution = instance.judgeCircle(input)
    print(solution)
