function solve(matrix) {

    function matrixPrinting(matrix) {
        for (let index = 0; index < matrix.length; index++) {
            console.log(matrix[index].join(' '));
        }
    }

    let firstDiagonalSum = 0;
    let secondDiagonalSum = 0;
    let column = 0;
    let changedMatrix = [];
    let diagonalCoordinates = [];

    for (let subArrIndex = 0; subArrIndex < matrix.length; subArrIndex++) {
        changedMatrix.push(matrix[subArrIndex].split(' '));
    }

    let endColumnIndex = changedMatrix[0].length - 1;
    

    for (let row = 0; row < matrix.length; row++) {
        firstDiagonalSum += Number(changedMatrix[row][column]);
        secondDiagonalSum += Number(changedMatrix[row][endColumnIndex]);
        diagonalCoordinates.push(`${row} ${column}`);
        diagonalCoordinates.push(`${row} ${endColumnIndex}`);
        column++;
        endColumnIndex--;
    }
    
    if (firstDiagonalSum == secondDiagonalSum) {
        for (let row = 0; row < changedMatrix.length; row++) {
            for (let col = 0; col < changedMatrix[row].length; col++) {
                if (!(diagonalCoordinates.includes(`${row} ${col}`))) {
                    changedMatrix[row][col] = firstDiagonalSum;
                }
            }
        }
        matrixPrinting(changedMatrix);
    } else {
        matrixPrinting(changedMatrix);
    }
}
