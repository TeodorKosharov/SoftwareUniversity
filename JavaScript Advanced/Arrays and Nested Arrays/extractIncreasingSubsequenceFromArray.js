function solve(arr) {
    let biggest = arr[0];
    let result = [arr[0]];

    for (let index = 1; index < arr.length; index++) {
        if (arr[index] > biggest) {
            biggest = arr[index];
            result.push(arr[index]);
        }
    }
    return result;
}
