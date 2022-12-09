function solve(matrix) {
    let isMagical = false;
    let sum = 0;
    let subArr = matrix[0];

    for (let index = 0; index < subArr.length; index++) {
        sum += subArr[index];
    }

    for (let index = 0; index < matrix.length; index++) {
        let currentSum = 0;
        for (let subIndex = 0; subIndex < matrix[index].length; subIndex++) {
            currentSum += matrix[index][subIndex];
        }
        currentSum == sum ? isMagical = true : isMagical = false;
        if (isMagical == false) break;
    }

    for (let index = 0; index < subArr.length; index++) {
        let currentSum = 0;
        for (let column = 0; column < matrix.length; column++) {
            currentSum += matrix[column][index];
        }
        currentSum == sum ? isMagical = true : isMagical = false;
        if (isMagical == false) break;
    }
    console.log(isMagical);
}
