function solve(arr) {
    let result = [];
    let step = Number(arr.pop());
    for (let index = 0; index < arr.length; index += step) {
        result.push(arr[index]);
    }
    console.log(result.join(' '));
}
