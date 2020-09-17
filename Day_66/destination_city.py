class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ends = []
        rest = []
        for path in paths:
            ends.append(path[-1])
            rest.append(path[0])
        print(ends, rest)
        for i in range(len(ends)):
            if ends[i] not in rest:
                destination = ends[i]
        return destination
