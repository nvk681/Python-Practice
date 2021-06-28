def rotate(matrix):
        for i in range(len(matrix)):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            matrix[i] = reversed(matrix[i])