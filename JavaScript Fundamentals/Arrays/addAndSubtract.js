function solve(arr) {
    let originalArrSum = 0;
    let modifiedArrSum = 0;

    for (let index = 0; index < arr.length; index++) {
        originalArrSum += arr[index];
        arr[index] % 2 == 0 ? arr[index] += index : arr[index] -= index;
        modifiedArrSum += arr[index];
    }
    console.log(arr);
    console.log(originalArrSum);
    console.log(modifiedArrSum);
}
