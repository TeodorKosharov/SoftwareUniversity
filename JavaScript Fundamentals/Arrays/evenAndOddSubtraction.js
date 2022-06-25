function solve(arr) {
    let evenSum = 0;
    let oddSum = 0;
    for (let index = 0; index < arr.length; index++) {
        arr[index] % 2 == 0 ? evenSum += arr[index] : oddSum += arr[index];
    }
    console.log(evenSum - oddSum);
}