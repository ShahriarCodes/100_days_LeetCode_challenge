class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = {}
        map2 = {}
        for num1 in nums1:
            if num1 in map1:
                map1[num1] += 1
            else:
                map1[num1]  = 1
        for num2 in nums2:
            if num2 in map2:
                map2[num2] += 1
            else:
                map2[num2]  = 1
        print(map1)
        print(map2)
        
        final = {}
        for key in map1:
            if key in map2:
                final[key] = min(map1[key],map2[key])
        print(final)
        
        result = []
        for key in final:
            result += [key]*final[key]
        return result
