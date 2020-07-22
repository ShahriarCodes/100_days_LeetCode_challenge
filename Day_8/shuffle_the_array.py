class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        new_list = []
        for i in range(n-1):
            new_list.append(nums[i])
            new_list.append(nums[i+n])

        return new_list


if __name__ == '__main__':

    nums = [2,5,1,3,4,7]
    n = 3
    instance = Solution()
    solution = instance.shuffle(nums , n)
    print(type(solution))
