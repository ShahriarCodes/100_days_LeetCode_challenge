class Solution:
    def countBits(self, num: int) -> List[int]:
        lst = [0,1,1]
        if num <= 2:
            return lst[:num+1]
        for i in range(3, num+1):
            if i%2 == 0:
                lst.append(lst[i//2])
            else:
                lst.append(lst[i//2]+1)
            
        return lst
