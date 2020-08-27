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

#faster
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxSoFar = arr[-1]
        arr[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = maxSoFar
            maxSoFar = max(maxSoFar, temp)
        return arr

if __name__ == '__main__':

    arr = [17,18,5,4,6,1]
    instance = Solution()
    solution = instance.replaceElements(arr)

    print(solution)
