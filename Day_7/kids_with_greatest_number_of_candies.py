class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        sorted_list = sorted(candies, reverse = True)
        return [candy + extraCandies >= sorted_list[0] for candy in candies]
