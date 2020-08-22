class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        # alphabet = '2abcdefghijklmnopqrstuvwxyz'
        # hashmap = {}
        # for i in range(1,27):
        #     if i > 9 :
        #         hashmap[str(i)+'#'] = alphabet[i]
        #     else:
        #         hashmap[str(i)] = alphabet[i]

        dict = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p', '17#': 'q', '18#': 'r', '19#': 's', '20#': 't', '21#': 'u', '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'}
        reversed_s = s[::-1]
        decrypt = ''
        # for index in range (len(reversed_s)):
        index = 0
        while index<len(reversed_s):
            if reversed_s[index] == "#":
                ss = reversed_s[index:index+3][::-1]
                decrypt += dict[ss]
                # print(ss)
                index += 3
            else:
                ss = reversed_s[index]
                decrypt += dict[ss]
                # print(reversed_s[index])
                index += 1

        return decrypt[::-1]


if __name__ == '__main__':

    s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    instance = Solution()
    solution = instance.freqAlphabets(s)

    print(solution)
    assert  solution == "abcdefghijklmnopqrstuvwxyz"

"10#11#12"[::-1]
