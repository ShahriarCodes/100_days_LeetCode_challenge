class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        output = [0]*num_people
        j = 0
        candy = 1
        while candies > 0:
            if candies < candy:
                output[j] += candies
            else : output [j] += candy
            j += 1
            if j > num_people-1:
                 j = 0
            candies -= candy
            candy += 1
        print(output)
        return output
        
        
