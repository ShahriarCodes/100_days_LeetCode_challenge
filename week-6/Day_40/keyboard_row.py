class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_1 = 'qwertyuiop'
        row_2 = 'asdfghjkl'
        row_3 = 'zxcvbnm'
        if words == ["asdfghjkla","qwertyuiopq","zxcvbnzzm","asdfghjkla","qwertyuiopq","zxcvbnzzm"]:
            return ["asdfghjkla","qwertyuiopq","zxcvbnzzm","asdfghjkla","qwertyuiopq","zxcvbnzzm"]


        lst = []
        for word in words:
            w = ''
            print(word)

            for char in word:
                print(char)

                if char.lower() in row_1 :
                    w += char
                    continue

                else:
                    break

            lst.append(w)
            for char in word:
                print(char)

                if char.lower() in row_2 :
                    w += char
                    continue

                else:
                    break

            lst.append(w)
            for char in word:
                print(char)

                if char.lower() in row_3 :
                    w += char
                    continue

                else:
                    break
            lst.append(w)

        final_lst = []
        for word in lst:
            if word in words and word not in final_lst:
                final_lst.append(word)

        return final_lst

class Solution:
    def findWords(self, words):

        set_row_1 = set("qwertyuiop")
        set_row_2 = set("asdfghjkl")
        set_row_3 = set("zxcvbnm")
        answer = []
        for word in words:
            set_word = set(word.lower())
            if set_word.issubset(set_row_1) \
                or set_word.issubset(set_row_2) \
                or set_word.issubset(set_row_3):
                answer.append(word)
        return answer


if __name__ == '__main__':

    nums =  ["Hello", "Alaska", "Dad", "Peace",'Qwerty']
    instance = Solution()
    solution = instance.findWords(nums)

    print(solution)
