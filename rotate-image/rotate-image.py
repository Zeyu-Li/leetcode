class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # x^T then reflect x along x
        
        length = len(matrix)
        
        # transpose (upper triangle flip)
        for i in range(length):
            for j in range(i, length):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        # flip in x
        for i in range(length):
            for j in range(length // 2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
        