class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        new_arr = []
        len_arr = len(arr)

        if len_arr == 1:
            return [-1]

        for i, num in enumerate(arr):
            if i < (len_arr-1):
                new_arr.append(max(arr[i+1:]))
            else:
                new_arr.append(-1)

        return new_arr


if __name__ == '__main__':

    arr = [17,18,5,4,6,1]
    instance = Solution()
    solution = instance.replaceElements(arr)

    print(solution)
