function solve(arr) {
    let result = [];
    for (let index = 0; index < arr.length; index++) {
        if (index % 2 == 0) result.push(arr[index]);
    }
    console.log(result.join(' '));
} 