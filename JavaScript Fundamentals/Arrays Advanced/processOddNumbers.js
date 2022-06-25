function solve(arr) {
    let result = [];

    for (let index = 0; index < arr.length; index++) {
        if (index % 2 == 1) result.push(arr[index] * 2);
    }
    result.reverse();
    console.log(result.join(' '));
}
