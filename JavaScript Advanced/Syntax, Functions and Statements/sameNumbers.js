function solve(num) {
    let numStr = String(num);
    let areIdentical = true;
    let sum = 0;

    for (let index = 0; index < numStr.length - 1; index++) {
        if (numStr[index] != numStr[index + 1]) areIdentical = false;
    }
    for (let el of numStr) sum += Number(el);
    
    console.log(areIdentical + '\n' + sum);
}