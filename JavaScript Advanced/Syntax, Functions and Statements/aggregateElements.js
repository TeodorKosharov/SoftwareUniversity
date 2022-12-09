function solve(arr) {
    let sum = 0;
    let inverseSum = 0;

    for (let el of arr) {
        sum += el;
        inverseSum += 1 / el;
    }
    console.log(sum);
    console.log(inverseSum);
    console.log(arr.join(''));
}
