class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        j = 0
        for i in range(2, len(s)+1, 2):
            print(s[j:i])
            if  s[j:i].count('L') == s[j:i].count('R'):
                count += 1
                j = i
        return count




if __name__ == '__main__':

    input = 'RLLRLRRL'
    instance = Solution()
    solution = instance.balancedStringSplit(input)
    print(solution)


'RLLRLRLR'.count('R').count('L')
