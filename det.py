def twobytwo(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]; # 2x2 matrix

def cal(coe, dim, matrix):
    if dim == 2:
        return coe * twobytwo(matrix);
        
    else:
        det = 0
        for i in range(dim):
            coe = matrix[0][i] * (-1)**i;
            submatrix = [];
            for j in range(1, dim):
                submatrix.append(matrix[j][:i] + matrix[j][i+1:]);
            # cal(coe, dim-1, submatrix, det)
            det += cal(coe, dim-1, submatrix);
    return det

def det(matrix):
    return cal(1, len(matrix), matrix);

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
# matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 9]];
# matrix = [[1, 2], [3, 4]]
print(det(matrix));
        
    


