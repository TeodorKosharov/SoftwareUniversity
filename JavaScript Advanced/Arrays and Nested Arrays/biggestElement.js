function solve(matrix) {
    let max = -10000000;
    for (let row = 0; row < matrix.length; row++) {
        for (let col = 0; col < matrix[row].length; col++) {
            if (matrix[row][col] > max) max = matrix[row][col];
        }
    }
    return max;
}
