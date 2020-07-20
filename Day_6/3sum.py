class Solution(object):
    # def _init__ (self):
    #     lst = []
    #

    def combinations(self,iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
        pool = tuple(iterable)
        n = len(pool)
        if r > n:
            return
        indices = range(r)
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
            yield tuple(pool[i] for i in indices)

    # def n_length_combo(lst, n):
    #
    #     if n == 0:
    #         return [[]]
    #
    #     l =[]
    #     for i in range(0, len(lst)):
    #
    #         m = lst[i]
    #         remLst = lst[i + 1:]
    #
    #         for p in n_length_combo(remLst, n-1):
    #             l.append([m]+p)
    #
    #     return l

    def threeSum(self, nums, lst , n):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums = [-1, 0, 1, 2, -1, -4]
        answer = self.combinations(nums, 3)
        return answer



        # from itertools import combinations
        #
        #
        # # Get all permutations of length 2
        # # and length 2
        # comb = combinations(nums, 3)
        #
        # comb_list = []
        # for i in list(comb):
        #     if sum(i)==0:
        #         comb_list.append(i)
        # return comb_list


if __name__ == '__main__':

    input = [-1, 0, 1, 2, -1, -4]
    instance = Solution()
    solution = instance.threeSum(input, input, 3)
    print(type(solution))





def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


comb = combinations([-1, 0, 1, 2, -1, -4],3)
for i in comb:
    print (i)
