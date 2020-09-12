#O(N)
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for c in letters:
            if c > target:
                return c
        return letters[0]

#O(log(N))
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]
