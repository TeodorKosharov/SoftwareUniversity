function solve(matrix) {
    let mainSum = 0;
    let secondarySum = 0;
    let colIndex = 0;

    for (let row = 0; row < matrix.length; row++) {
        mainSum += matrix[row][colIndex];
        secondarySum += matrix[row][matrix.length - 1 - colIndex];
        colIndex++;
    }
    console.log(`${mainSum} ${secondarySum}`);
}
