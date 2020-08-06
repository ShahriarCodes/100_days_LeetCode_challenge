class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        s = s.split(' ')

        final = ''
        i = len(s) - 1
        while i >= 0:
            final += s[i] + ' '
            i -= 1
        final = final [:-1]
        return final






if __name__ == '__main__':

    nums = "Let's take LeetCode contest"
    instance = Solution()
    solution = instance.reverseWords(nums)

    print(solution)
"Let's take LeetCode contest".pop()
