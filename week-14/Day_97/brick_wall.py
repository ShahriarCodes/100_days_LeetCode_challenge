class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_frequency = {}

        max_frequency = 0
        
        for row in range(len(wall)):
        # for(int row=0; row<wall.size(); row++)        //Iterating through each row

            edge_postion = 0     
            for brick_no in range(len(wall[row])-1):
            # for(int brick_no=0; brick_no< wall[row].size() -1; brick_no++)    //Iterating through each brick inside a row
            # { 
                current_brick_length = wall[row][brick_no]
                
                edge_postion = edge_postion + current_brick_length 
                
                if edge_postion not in edge_frequency:
                    edge_frequency[edge_postion]  = 1 
                else: edge_frequency[edge_postion]  += 1
                
                max_frequency = max(edge_frequency[edge_postion],max_frequency)
        return len(wall) - max_frequency
