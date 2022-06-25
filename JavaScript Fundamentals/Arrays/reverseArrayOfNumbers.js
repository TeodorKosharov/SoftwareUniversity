function solve(n, arr) {
    let newArr = [];
    let index = 0;
    for (let i = 1; i <= n; i++) {
        newArr.push(arr[index]);
        index++;
    }
    let reversedArr = [];
    for (let idx = newArr.length - 1; idx >= 0; idx--) {
        reversedArr.push(newArr[idx]);
    }

    console.log(reversedArr.join(' '));
}
