class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = sorted(strs, key = len)

        common = ''
        for i, char in enumerate(strs[0]):

            if all(char == word[i] for word in strs) == True:
                common += char
            else:
                break
        return common





if __name__ == '__main__':

    input = ["aa","a"]
    # x = str("()[][]")
    instance = Solution()
    solution = instance.longestCommonPrefix(input)
    print(solution)
