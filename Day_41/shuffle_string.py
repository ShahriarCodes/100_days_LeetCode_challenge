class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List
        :rtype: str
        """
        shuffled = ['x']*(len(s))
        print(shuffled)

        for char, index in zip(s, indices):
            shuffled[index] = char

        return ''.join(shuffled)



if __name__ == '__main__':

    s = 'art'
    indices = [1,0,2]

    s = 'codeleet'
    # indices = [4,5,6,7,0,2,1,3]
    
    instance = Solution()
    solution = instance.restoreString(s, indices)

    print(solution)
