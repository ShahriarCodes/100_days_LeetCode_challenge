class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_list = []
        for s in S:
            if s == '#':
                if len(s_list) > 0:
                    s_list.pop()
                else: continue
            else:
                s_list.append(s)
        
                
        t_list = []
        for t in T:
            if t == '#':
                if len(t_list) > 0:
                    t_list.pop()
                else: continue
            else:
                t_list.append(t)   
        
        print(s_list, t_list)
        
        return s_list == t_list
