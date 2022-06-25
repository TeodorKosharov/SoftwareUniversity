function solve(firstArr, secondArr) {
    let sum = 0;
    let areArrsDifferent = false;
    let searchIndex = 0;

    for (let index = 0; index < firstArr.length; index++) {
        sum += Number(firstArr[index]);
        searchIndex = index;

        firstArr[index] == secondArr[index] ? areArrsDifferent = false : areArrsDifferent = true;
        if (areArrsDifferent) break;
    }

    if (areArrsDifferent == true) {
        console.log(`Arrays are not identical. Found difference at ${searchIndex} index`);
    } else {
        console.log(`Arrays are identical. Sum: ${sum}`);
    }
}
