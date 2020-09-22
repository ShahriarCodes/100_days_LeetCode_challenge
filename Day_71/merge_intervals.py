class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals = sorted(intervals, key = lambda interval: interval[0])
        
        new_list = []
        new_list.append(intervals[0])
        for i in range(len(intervals)):
            if new_list[-1][1] >= intervals[i][0]:
                new_list[-1][1] = max(new_list[-1][1], intervals[i][1])
            else:
                new_list.append(intervals[i])
        return new_list
