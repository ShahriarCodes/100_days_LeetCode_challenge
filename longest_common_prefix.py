class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = sorted(strs, key = len)

        common = ''
        for i, char in enumerate(strs[0]):
            # if char in [word[i] for j in range]
            if all(char == word[i] for word in strs) == True:
                common += char
            else:
                break
        return common


    # def all_same(items):
    #     return all(x == items[0] for x in items)


if __name__ == '__main__':

    input = ["aa","a"]
    # x = str("()[][]")
    instance = Solution()
    solution = instance.longestCommonPrefix(input)
    print(solution)
