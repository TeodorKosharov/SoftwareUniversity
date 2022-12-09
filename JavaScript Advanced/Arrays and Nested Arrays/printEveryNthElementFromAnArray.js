function solve(arr, step) {
    let result = [arr[0]];
    for (let index = step; index < arr.length; index += step) result.push(arr[index]);
    return result;
}
