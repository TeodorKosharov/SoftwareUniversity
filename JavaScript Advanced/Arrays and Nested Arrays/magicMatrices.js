function solve(matrix) {
    let rowsSums = [];
    let colsSums = [];

    for (let row = 0; row < matrix.length; row++) {
        let currentRowSum = 0;
        for (let col = 0; col < matrix[row].length; col++) {
            currentRowSum += matrix[row][col];
        }
        rowsSums.push(currentRowSum);
    }

    for (let col = 0; col < matrix.length; col++) {
        let currentColSum = 0;
        for (let row = 0; row < matrix.length; row++) {
            currentColSum += matrix[row][col];
        }
        colsSums.push(currentColSum);
    }

    let allSums = rowsSums.concat(colsSums);
    let element = allSums[0];
    allSums.filter(x => x === element).length === allSums.length ? console.log(true) : console.log(false);
}
