class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        lst = []
        e_pos = - len(S)
        
        i = 0
        while i < len(S):
            if S[i] == C:
                e_pos = i
            lst.append(i - e_pos)
            i += 1
        
        i = len(S) - 1
        while i >= 0:
            if S[i] == C:
                e_pos = i
            lst[i] = min(lst[i], abs(e_pos - i))
            i -= 1
        return lst
            
