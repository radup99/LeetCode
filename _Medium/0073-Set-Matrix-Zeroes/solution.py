class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rowList = []
        colList = []

        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == 0:
                    rowList.append(i)
                    colList.append(j)
        
        for i in range(0,m):
            for j in range(0,n):
                if i in rowList or j in colList:
                    matrix[i][j] = 0
