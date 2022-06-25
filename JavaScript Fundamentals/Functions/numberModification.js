function solve(number) {
    let numStr = String(number);

    while(true) {
        let digitsSum = 0;
        for (let digit of numStr) digitsSum += Number(digit);

        if (digitsSum / numStr.length > 5) break;
        else {
            numStr += '9';
        }
    }
    console.log(numStr);
}
