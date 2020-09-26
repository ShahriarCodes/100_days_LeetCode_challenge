#Step 1
#First find all the minimum elements in row and append it to res[] array.
#Step 2
# Then find all maximum in columns and append it to another array.
#Step 3
# Find Common Elements
class Solution(object):
    def luckyNumbers (self, matrix):
        res,list2,result = [],[],[]
		#Step 1
        for i in matrix:
            res.append(min((i)))
		#Step 2
        for col in range(len(matrix[0])): 
            col_max = matrix[0][col]  
            for row in range(1, len(matrix)):  
                col_max = max(col_max, matrix[row][col]) 
            list2.append(col_max)
		#Step 3
        for i in res:
            if i in list2:
                result.append(i)
        return result
        
